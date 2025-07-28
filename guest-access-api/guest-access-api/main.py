from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Sample guest data (normally fetched from a database)
guest_db = {
    "QR123": {"name": "John Doe", "event": "State Ceremony", "status": "confirmed"},
    "QR456": {"name": "Jane Smith", "event": "Press Conference", "status": "pending"}
}

class QRCode(BaseModel):
    code: str

@app.post("/check-in/")
def check_in(qr: QRCode):
    guest = guest_db.get(qr.code)
    if not guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    return {"message": "Access granted", "guest": guest}
