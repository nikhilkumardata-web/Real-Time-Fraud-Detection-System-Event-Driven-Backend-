transactions = []

def save(txn):
    transactions.append(txn)

def get_all():
    return transactions
