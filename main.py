from fastapi import FastAPI
from pydantic import BaseModel

from model.manager import Manager

app = FastAPI()

class SampleInput(BaseModel):
    age: str
    income: str
    student: str
    credit_rating: str
    job: str
    married: str



manager = Manager()

@app.post("/predict")
def predict(sample: SampleInput):

    sample_dict = sample.dict()
    result = manager.predictor.predictor(sample_dict)
    return {"prediction": result}

@app.on_event("startup")
def startup_event():

    manager.run()
