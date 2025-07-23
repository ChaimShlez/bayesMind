import httpx
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from naiveBayesClassifier import NaiveBayesClassifier

app = FastAPI()


class SampleInput(BaseModel):
    age: str
    income: str
    student: str
    credit_rating: str
    job: str
    married: str


@app.post("/predict")
async def predict(sample: SampleInput):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get("http://model-service:8000/model")
            resp.raise_for_status()
            payload = resp.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching model: {e}")

    model = payload["model"]
    label = payload["label"]
    classifier = NaiveBayesClassifier(label, model)
    result = classifier.predictor(sample.dict())
    return {"prediction": result}
