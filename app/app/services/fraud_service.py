from app.models.ml_model import predict_fraud
from app.utils.rules import rule_engine
from app.utils.logger import log_transaction

def process_transaction(txn):
    log_transaction(txn)

    rule_flag = rule_engine(txn.amount)
    ml_flag = predict_fraud(txn.amount)

    is_fraud = rule_flag or ml_flag

    if is_fraud:
        return {"status": "Fraud detected"}

    return {"status": "Safe"}
