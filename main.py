from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/api/health", tags=["Health"])
async def health():
    return {
        "status" : "OK!"
    }