from contextlib import asynccontextmanager

from fastapi import FastAPI
from manager import Manager




modal_naive = None
label = None

manager = Manager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    global modal_naive, label
    modal_naive, label = manager.run()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/model")
def get_model():
    if modal_naive is None or label is None:
        return {"error": "Model is not trained yet."}
    return {"model": modal_naive, "label": label}
