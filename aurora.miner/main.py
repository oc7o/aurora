import requests
import json
import hashlib
import datetime
import sys


PRIVATE_KEY = ""
PUBLIC_KEY = ""

# utils

def attributes2string(*args):
    string = ""
    if len(args) > 0:
        for arg in args:
            string += "/" + str(arg)
        string = string[1:]

    return string


def hash_string(string):
    return hashlib.sha256(string.encode("utf-8")).hexdigest()

def transactions_hash(transactions):
    string = ""
    if len(transactions) > 0:
        for transaction in transactions:
            string += "$" + transaction
        string = string[1:]
    return hashlib.sha256(string.encode("utf-8")).hexdigest()

def match_difficulty(hash_string, difficulty):
    start = difficulty * "0"
    return hash_string.startswith(start)

def block_hash(block, transactions):
    block_string = attributes2string(
        block["prev_block"],
        block["transactions_counter"],
        block["transactions_hash"],
        block["timestamp"],
        block["nonce"],
    )
    block_hash = hash_string(block_string)
    # if block_hash.startswith("00000"):
    #     print(block_string)
    return block_hash


# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
# response.json()
# response.status_code


class Miner():
    # Config
    api_url = "http://blockchain.aurora-coin.tk/api/"
    headers =  {"Content-Type":"application/json"}
    private_key = ""
    public_key = ""
    difficulty = 7
    # running = False

    def __init__(self, private, pubic) -> None:
        self.private_key = private
        self.public_key = pubic

    def generate_bonus_transaction(self):
        # Create Bonus Transaction

        bonus_transcation = {
            "from_address": 64*"0",
            "to_address": self.public_key,
            "amount": 50,
            "fee": 0
        }
        bonus_transcation_request = requests.post(self.api_url + 'transaction/', data=json.dumps(bonus_transcation), headers=self.headers)
        nonce = requests.get(self.api_url + "address_nonce/" + 64*"0").json()
        transaction_string = attributes2string(
            nonce,
            64 * "0",
            bonus_transcation['to_address'],
            bonus_transcation['amount'],
            bonus_transcation['fee'],
        )
        transaction_hash = hash_string(transaction_string)
        return transaction_hash

    def get_pool_transactions(self):
        # Get random block transactions from pool
        pool = requests.get(self.api_url + 'transaction/pool/').json()
        transactions = []
        for transaction in pool:
            if len(transactions) >= 9:
                break
            transactions.append(transaction['transaction_hash'])
        
        bonus_transaction = self.generate_bonus_transaction()
        if bonus_transaction not in transactions:
            transactions.append(bonus_transaction)
        return (transactions)

    def generate_block(self):
        blocks = requests.get(self.api_url + 'block/').json()
        last_block = 64*"0"
        if len(blocks) > 0:
            last_block = blocks[-1]['block_hash']
        transactions = self.get_pool_transactions()

        block = {
            "prev_block": last_block,
            "transactions_counter": len(transactions),
            "transactions_hash": transactions_hash(transactions),
            "timestamp": int(datetime.datetime.now().timestamp()),
            "nonce": 0,
        }

        while not match_difficulty(block_hash(block, transactions), self.difficulty):
            block['nonce'] += 1
        self.publish_block(block, transactions)

    def publish_block(self, block, transactions):
        data = {
            'timestamp': block['timestamp'],
            'nonce': block['nonce'],
            'transactions': transactions,
        }
        # print(data)
        request = requests.post(self.api_url + "block/", data=json.dumps(data), headers=self.headers)
        print("Block generated!")
        # print(request.json())

    def run(self):
        while True:
            self.generate_block()
            


### Start

miner = Miner(PRIVATE_KEY, PUBLIC_KEY)
miner.generate_block()
