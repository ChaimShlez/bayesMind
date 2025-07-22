import json

from fastapi import FastAPI
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
def predict(sample: SampleInput):

    sample_dict = sample.dict()

    path_model = "data_model/model.json"
    path_label = "data_model/label.json"
    with open(path_model, "r") as f:
        model = json.load(f)

    with open(path_label, "r") as f:
        label = json.load(f)
    classifier=NaiveBayesClassifier(label,model)
    result = classifier.predictor(sample_dict)
    return {"prediction": result}
