import binascii
import json

import pytest
from aurora.blockchain.models import Transaction
from nacl.signing import SigningKey
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TransactionTests(APITestCase):
    def test_create_transaction(self):
        from_address_private = SigningKey.generate()
        from_address_public = from_address_private.verify_key
        from_address_public_string = binascii.hexlify(from_address_public.encode()).decode()

        to_address_private = SigningKey.generate()
        to_address_public = to_address_private.verify_key
        to_address_public_string = binascii.hexlify(to_address_public.encode()).decode()

        transaction = {
            "nonce": 0,
            "from_address": from_address_public_string,
            "to_address": to_address_public_string,
            "amount": 20,
            "fee": 5,
        }
        message = str(json.dumps(transaction, separators=(",", ":")))
        print("message str", message)
        # print("m hex", binascii.hexlify(message.encode()).decode())
        print("from key hex", binascii.hexlify(from_address_private.encode()).decode())
        singed = from_address_private.sign(message.encode())
        signature = binascii.hexlify(singed.signature).decode()
        print("signature hex", signature)
        data = transaction
        del data["nonce"]
        data.update({"signature": signature})

        url = reverse("api:transaction-list")
        response = self.client.post(url, data, format="json")
        assert response.status_code == 201
        assert Transaction.objects.filter(from_address=from_address_public_string, nonce=0).exists()
