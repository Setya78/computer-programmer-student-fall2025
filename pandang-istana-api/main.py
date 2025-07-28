# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import uuid

app = FastAPI()

# Temporary in-memory storage for demo
guest_db = {}

class Guest(BaseModel):
    name: str
    institution: str
    email: str

@app.post("/register_guest")
def register_guest(guest: Guest):
    guest_id = str(uuid.uuid4())
    guest_db[guest_id] = {
        "name": guest.name,
        "institution": guest.institution,
        "email": guest.email,
        "qr_code": f"QR-{guest_id[:8]}"
    }
    return {"guest_id": guest_id, "qr_code": guest_db[guest_id]["qr_code"]}

@app.get("/guest/{guest_id}")
def get_guest(guest_id: str):
    if guest_id not in guest_db:
        return {"error": "Guest not found"}
    return guest_db[guest_id]
