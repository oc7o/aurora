import binascii
import json

from aurora.blockchain.models import Block, Transaction
from aurora.blockchain.utils import (
    get_address_balance,
    get_address_nonce,
    match_difficulty,
)
from django.conf import settings
from django.utils.timezone import datetime
from nacl.signing import VerifyKey
from rest_framework import serializers


class TransactionsField(serializers.StringRelatedField):
    """
    This is a custom field, representing a Blocks transactions
    """

    # this is simply to override the function to do nothing, cause I only need the data and this was (in my case) the easiest way
    def to_internal_value(self, data):
        pass


class BlockSerializer(serializers.ModelSerializer):
    """
    Here gets the received data from the Views validated and handeled
    """

    transactions = TransactionsField(many=True)  # see TransactionsField
    prev_block = serializers.CharField(
        source="parent", read_only=True
    )  # to rename the MPTTModel

    class Meta:
        model = Block
        fields = [
            "timestamp",
            "nonce",
            "transaction_counter",
            "transactions_hash",
            "block_hash",
            "transactions",
            "pk",
            "prev_block",
        ]
        read_only_fields = [
            "transaction_counter",
            "transactions_hash",
            "block_hash",
            "pk",
            "prev_block",
        ]

    def validate_timestamp(self, value):
        if self.Meta.model.objects.count() != 0:
            valid_timestamp = (
                int(value) > int(self.Meta.model.objects.last().timestamp)
                and int(value) < int(datetime.now().timestamp()) + 3600
                and int(value) > int(datetime.now().timestamp()) - 3600
            )  # timestamp is newer than prev blocks timestamp and +/- hour accurat
            if not valid_timestamp:
                raise serializers.ValidationError("Timestamp is not valid.")
        return value

    def create(self, validated_data):
        all_transactions = {}
        # get transactions dict of all the 'blockless' transactions with transaction_hash as key and transactions object as value
        # this is not verry efficient but I cant filter for a models function value
        for transaction in Transaction.objects.filter(block=None):
            all_transactions.update(
                {transaction.transaction_hash(): transaction}
            )
        # to filter the transactions which get into the block
        transactions = [
            all_transactions[transaction]
            for transaction in self.context["request"].data["transactions"]
        ]
        del validated_data["transactions"]
        block = self.Meta.model(**validated_data)

        # if genesis block
        if Block.objects.count() == 0:
            block.parent = None
        else:
            block.parent = Block.objects.last()

        # I have to safe the block, before I add the transactions to it, because It's difficutlt to handle OneToMany relations instead of ManyToOne
        # The weakness is, that there could be an invalid block in the database for a short moment
        # There are ways to solve this problem, but it would be a lot of additional work
        block.save()
        block.transactions.set(transactions)
        # If there is no/more than one bonus transaktion
        if block.transactions.filter(from_address=64 * "0").count() != 1:
            block.delete()
            raise serializers.ValidationError(
                "There must be ONE bonus transaction."
            )
        # if the block reward is not equal to the block bonus
        if (
            block.transactions.get(from_address=64 * "0").amount
            + block.transactions.get(from_address=64 * "0").fee
            != settings.BONUS
        ):
            block.delete()
            raise serializers.ValidationError("Your bonus is not valid.")
        # if the block doesn't match the difficulty
        if not match_difficulty(block.block_hash(), settings.DIFFICULTY):
            block.delete()
            raise serializers.ValidationError(
                "This block is not difficult enough."
            )
        return block


class TransactionSerializer(serializers.ModelSerializer):
    """
    Here gets the received data from the Views validated and handeled
    """

    # this is an additional wo field to check the transactions validity
    signature = serializers.CharField(
        write_only=True, required=False, allow_null=True
    )
    block = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = [
            "nonce",
            "from_address",
            "to_address",
            "amount",
            "fee",
            "block",
            "transaction_hash",
            "signature",
        ]
        read_only_fields = ["nonce", "block", "transaction_hash"]

    def create(self, validated_data):
        signature = None
        # if there is a signature => it's no bonus transaction
        if "signature" in validated_data.keys():
            # if it contains invalid data: delete it
            if (
                validated_data["signature"] == ""
                or validated_data["signature"] is None
            ):
                del validated_data["signature"]

        # if there is a signature save it and delete it from the validated_data
        if "signature" in validated_data.keys():
            signature = binascii.unhexlify(
                validated_data["signature"].encode()
            )
            del validated_data["signature"]

        # if it's a bonus transaction
        # Here is the problem, that one could spam many junk bonus transaktions to the node, a check and regular pool deletions could be meaningful
        if validated_data["from_address"] == 64 * "0":
            validated_data["from_address"] = 64 * "0"
            validated_data["nonce"] = get_address_nonce(
                validated_data["from_address"]
            )
            # This could be changed
            # An option could be to make it dynamic
            validated_data["amount"] = 50
            validated_data["fee"] = 0
            #

            if Transaction.objects.filter(
                from_address=validated_data["from_address"],
                to_address=validated_data["to_address"],
                nonce=validated_data["nonce"],
            ).exists():
                raise serializers.ValidationError(
                    "This Transaction already exists."
                )

            transaction = self.Meta.model(**validated_data)
            transaction.save()
            return transaction

        # if it's a 'normal' transaction
        elif signature:
            nonce = get_address_nonce(validated_data["from_address"])

            transaction = {"nonce": nonce}
            transaction.update(validated_data)
            # the message is the raw transaction string
            message = str(json.dumps(transaction, separators=(",", ":")))

            from_public_address_bytes = binascii.unhexlify(
                validated_data["from_address"].encode()
            )
            # the VerifyKey Object
            from_address = VerifyKey(from_public_address_bytes)
            # here the transaction gets verified by the signature
            from_address.verify(message.encode(), signature)
            transaction = self.Meta.model(**transaction)

            # if transaction empty or negative
            if transaction.amount + transaction.fee <= 0:
                raise serializers.ValidationError(
                    "You can't create empty transactions."
                )

            # if the address doesn't have enough coins to pay
            if not (
                transaction.amount + transaction.fee
                <= get_address_balance(transaction.from_address)
            ):
                raise serializers.ValidationError(
                    "You don't have enough coins."
                )

            # if transaction already exists (to prevent crashes)
            if transaction.transaction_hash() in [
                t.transaction_hash() for t in Transaction.objects.all()
            ]:
                raise serializers.ValidationError(
                    "This transaction already exists."
                )

            transaction.save()
            return transaction
        raise serializers.ValidationError("Unknown Error :/")
