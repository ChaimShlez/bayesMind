from fastapi import FastAPI
from sklearn.metrics import confusion_matrix

app=FastAPI()


@app.get("/confusionMatrix")
def Display_confusion_matrix():
    pass
