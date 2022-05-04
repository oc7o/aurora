import datetime

import pytest
from aurora.blockchain.models import Block, Transaction
from aurora.blockchain.utils import match_difficulty
from aurora.tests.factories import TransactionFactory
from django.conf import settings
from nacl.signing import SigningKey
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class BlockTests(APITestCase):
    def test_create_block(self):
        transaction_objects = [TransactionFactory() for i in range(10)]
        transaction_strings = [t.transaction_hash() for t in transaction_objects]
        timestamp = int(datetime.datetime.now().timestamp())
        nonce = 0

        block = Block()
        block.timestamp = timestamp
        block.nonce = 0
        block.save()
        block.transactions.set(transaction_objects)
        while not match_difficulty(block.block_hash(), settings.DIFFICULTY):
            nonce += 1
            block.nonce = nonce
        block.delete()

        data = {"timestamp": timestamp, "nonce": nonce, "transactions": transaction_strings}

        url = reverse("api:block-list")
        response = self.client.post(url, data, format="json")
        assert response.status_code == 201
        assert Block.objects.filter(timestamp=timestamp).exists()
