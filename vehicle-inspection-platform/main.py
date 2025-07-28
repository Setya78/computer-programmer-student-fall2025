from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Vehicle Inspection API is live"}
