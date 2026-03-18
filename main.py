from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
import uuid

app = FastAPI(title="Payment DAI API", version="1.0.0")

# Models
class Transaction(BaseModel):
    id: str
    amount: float
    currency: str
    status: str
    recipient_address: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class CreateTransactionRequest(BaseModel):
    amount: float
    currency: str = "DAI"
    recipient_address: str
    description: Optional[str] = None

class TransactionResponse(BaseModel):
    id: str
    amount: float
    currency: str
    status: str
    recipient_address: str
    description: Optional[str] = None
    created_at: str
    updated_at: str

# In-memory storage (replace with database)
transactions_db = {}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "Payment DAI API"}

@app.post("/transactions", response_model=TransactionResponse)
async def create_transaction(request: CreateTransactionRequest):
    """Create a new transaction"""
    transaction_id = str(uuid.uuid4())
    now = datetime.utcnow()
    
    transaction = {
        "id": transaction_id,
        "amount": request.amount,
        "currency": request.currency,
        "status": "pending",
        "recipient_address": request.recipient_address,
        "description": request.description,
        "created_at": now,
        "updated_at": now
    }
    
    transactions_db[transaction_id] = transaction
    
    return TransactionResponse(
        **transaction,
        created_at=now.isoformat(),
        updated_at=now.isoformat()
    )

@app.get("/transactions/{transaction_id}", response_model=TransactionResponse)
async def get_transaction(transaction_id: str):
    """Retrieve a transaction by ID"""
    if transaction_id not in transactions_db:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    transaction = transactions_db[transaction_id]
    return TransactionResponse(
        **transaction,
        created_at=transaction["created_at"].isoformat(),
        updated_at=transaction["updated_at"].isoformat()
    )

@app.get("/transactions", response_model=List[TransactionResponse])
async def list_transactions(status: Optional[str] = None, limit: int = 10):
    """List all transactions with optional filtering"""
    transactions = list(transactions_db.values())
    
    if status:
        transactions = [t for t in transactions if t["status"] == status]
    
    return [
        TransactionResponse(
            **t,
            created_at=t["created_at"].isoformat(),
            updated_at=t["updated_at"].isoformat()
        )
        for t in transactions[:limit]
    ]

@app.patch("/transactions/{transaction_id}/status")
async def update_transaction_status(transaction_id: str, status: str):
    """Update transaction status"""
    if transaction_id not in transactions_db:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    valid_statuses = ["pending", "completed", "failed", "cancelled"]
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail=f"Invalid status. Must be one of {valid_statuses}")
    
    transaction = transactions_db[transaction_id]
    transaction["status"] = status
    transaction["updated_at"] = datetime.utcnow()
    
    return {"message": "Status updated", "transaction_id": transaction_id, "new_status": status}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)