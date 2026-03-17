import datetime

def log_transaction(txn):
    print(f"[{datetime.datetime.now()}] {txn}")
