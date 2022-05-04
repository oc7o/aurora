from .models import Block, Transaction


# Check if the given hash_string matches the given difficulty
def match_difficulty(hash_string, difficulty):
    start = difficulty * "0"
    return hash_string.startswith(start)


# gets the address Nonce (the number of transactions a address made)
def get_address_nonce(address):
    nonce = 0
    for transaction in Transaction.objects.all():
        if transaction.from_address == address and transaction.block != None:
            nonce += 1

    print(nonce)
    return nonce


# gets the balance of an address
def get_address_balance(address):
    balance = 0

    for transaction in Transaction.objects.all():
        if address == transaction.to_address and transaction.block != None:
            balance += transaction.amount
        if address == transaction.from_address:
            balance -= transaction.amount + transaction.fee
    print(balance)

    for block in Block.objects.all():
        if (
            block.transactions.filter(from_address=64 * "0").exists()
            and block.transactions.get(from_address=64 * "0").to_address
            == address
        ):
            for block_transaction in block.transactions.all():
                balance += block_transaction.fee

    print(balance)
    return balance
