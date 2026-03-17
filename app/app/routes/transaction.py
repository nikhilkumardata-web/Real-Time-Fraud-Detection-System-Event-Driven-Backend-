from fastapi import APIRouter
from app.schemas.transaction_schema import Transaction
from app.services.fraud_service import process_transaction

router = APIRouter()

@router.post("/transaction")
def check_transaction(txn: Transaction):
    return process_transaction(txn)
