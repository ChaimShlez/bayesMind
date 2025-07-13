import json
from typing import Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel

from predictor.naiveBayesPredictor import NaiveBayesPredictor


class PredictorRequest(BaseModel):
    target: Dict[str, Any]
app=FastAPI()

@app.post("/predictor")
async def predictor(data:PredictorRequest):
    target=data.target

    with open("model.json", "r") as f:
        model_dict = json.load(f)

    with open("label.json", "r") as f:
        label_dict = json.load(f)

    # label_test = pd.Series(data.labels)
    predict=NaiveBayesPredictor(model_dict,label_dict)
    result = predict.predictor(target)

    return {"prediction": result}
