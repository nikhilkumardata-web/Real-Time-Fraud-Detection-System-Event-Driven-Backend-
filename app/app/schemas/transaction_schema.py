from pydantic import BaseModel

class Transaction(BaseModel):
    amount: float
    location: str
    device: str
