from fastapi import FastAPI
from manager import Manager

app = FastAPI()


modal_naive = None
label = None

manager = Manager()

@app.on_event("startup")
def startup_event():
    global modal_naive, label

    modal_naive, label = manager.run()

@app.get("/model")
def get_model():
    if modal_naive is None or label is None:
        return {"error": "Model is not trained yet."}
    return {"model": modal_naive, "label": label}
