import hashlib

from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


def attributes2string(*args):
    string = ""
    if len(args) > 0:
        for arg in args:
            string += "/" + str(arg)
        string = string[1:]

    return string


def hash_string(string):
    return hashlib.sha256(string.encode("utf-8")).hexdigest()


class Transaction(models.Model):
    """
    Aurora Transaction Model
    """

    nonce = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Number Only Once senders count of transactions"),
        help_text=_("format: Int"),
    )
    from_address = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name=_("Senders Public Addresss"),
        help_text=_("format: required, max-64"),
    )  # from_address
    to_address = models.CharField(
        max_length=64,
        blank=False,
        null=False,
        verbose_name=_("Resceivers Public Addresss"),
        help_text=_("format: required, max-64"),
    )  # to_address
    amount = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Transaction's amount"),
        help_text=_("format: Int"),
    )  # amount
    fee = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Transaction's fee"),
        help_text=_("format: Int"),
    )

    block = models.ForeignKey(
        "blockchain.Block",
        related_name="transactions",
        verbose_name=_("Transaction's block"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )  # block

    def transaction_hash(self):
        transaction_string = attributes2string(
            self.nonce,
            self.from_address,
            self.to_address,
            self.amount,
            self.fee,
        )
        transaction_hash = hash_string(transaction_string)
        return transaction_hash

    def __str__(self) -> str:
        return self.transaction_hash()


class Block(MPTTModel):
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="next_block",
        null=True,
        blank=True,
        unique=True,
        verbose_name=_("previous block"),
        help_text=_("format: not required, unique"),
    )

    timestamp = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Block's timestamp"),
        help_text=_("format: maximum time 9999999999"),
    )  # int(datetime.datetime.now().timestamp())
    nonce = models.IntegerField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Number Only Once, for mining a block"),
        help_text=_("format: Int"),
    )  # find out with bruteforcing

    def transaction_counter(self):
        return self.transactions.count()

    # instead of using a merkle root
    def transactions_hash(self):
        string = ""
        if self.transaction_counter() > 0:
            for transaction in self.transactions.all():
                string += "$" + transaction.transaction_hash()
            string = string[1:]
        return hashlib.sha256(string.encode("utf-8")).hexdigest()

    def block_hash(self):
        prev_block_hash = self.parent
        if prev_block_hash == None:
            prev_block_hash = "0000000000000000000000000000000000000000000000000000000000000000"

        block_string = attributes2string(
            prev_block_hash,
            self.transaction_counter(),
            self.transactions_hash(),
            self.timestamp,
            self.nonce,
        )
        block_hash = hash_string(block_string)
        return block_hash

    def __str__(self) -> str:
        return self.block_hash()
