# backend/app/models.py

from pydantic import BaseModel

class PredictRequest(BaseModel):
    title: str
    text: str

class PredictResponse(BaseModel):
    prediction: str
    confidence: float
