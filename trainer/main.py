from typing import Any, Dict, List
import json
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
from trainer.evaluator import Evaluator
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


    with open("model.json", "w") as f:
        json.dump(modal_naive, f)

    with open("label.json", "w") as f:
        json.dump(label, f)
    return {"message": "Model trained successfully"}





@app.post("/evaluator")
async def evaluator(data:EvaluatorRequest):
    df_test=pd.DataFrame(data.features)
    label_test = pd.Series(data.labels)

    with open("model.json", "r") as f:
        model_dict = json.load(f)

    with open("label.json", "r") as f:
        label_dict = json.load(f)

    # label_test = pd.Series(data.labels)
    eveluter=Evaluator(model_dict,label_dict)
    eveluter.Evolution_train(df_test,label_test)
