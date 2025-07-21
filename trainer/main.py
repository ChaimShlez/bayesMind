from typing import Any, Dict, List
import json
import os
import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from .evaluator import Evaluator
from trainer.naiveBayesTrainer import NaiveBayesTrainer

app = FastAPI()

class TrainRequest(BaseModel):
    features: List[Dict[str, Any]]

    labels: Dict[str, Any]

class EvaluatorRequest(BaseModel):
    features: List[Dict[str, Any]]
    labels:List[Any]
    # labels: Dict[str, Any]


@app.post("/train")
async def train(data: TrainRequest):
    df = pd.DataFrame(data.features)


    label = data.labels

    trainer = NaiveBayesTrainer(df, label)
    modal_naive=trainer.train()


    path_model  = "/app/output/json/model.json"
    with open(path_model, "w") as f:
        json.dump(modal_naive, f)

    path_label  = "/app/output/json/label.json"
    with open(path_label, "w") as f:
        json.dump(label, f)

    return {"train_status": "OK"}


@app.post("/evaluator")
async def evaluator(data:EvaluatorRequest):
    df_test=pd.DataFrame(data.features)
    label_test = pd.Series(data.labels)

    path_model = "/app/output/json/model.json"
    path_label = "/app/output/json/label.json"
    with open( path_model  , "r") as f:
        model_dict = json.load(f)

    with open(path_label, "r") as f:
        label_dict = json.load(f)

    # label_test = pd.Series(data.labels)
    eval=Evaluator(model_dict,label_dict)
    accuracy = eval.Evolution_train(df_test, label_test)

    return {"accuracy": accuracy}



if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8002)
