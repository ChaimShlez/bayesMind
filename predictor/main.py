import json
from typing import Dict, Any
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from naiveBayesPredictor import NaiveBayesPredictor


class PredictorRequest(BaseModel):
    target: Dict[str, Any]
app=FastAPI()

@app.post("/predictor")
async def predictor(data:PredictorRequest):
    target=data.target

    path_model = "/app/output/json/model.json"
    path_label = "/app/output/json/label.json"
    with open(path_model, "r") as f:
        model_dict = json.load(f)

    with open(path_label, "r") as f:
        label_dict = json.load(f)

    # label_test = pd.Series(data.labels)
    predict=NaiveBayesPredictor(model_dict,label_dict)
    result = predict.predictor(target)

    return {"prediction": result}
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8003)