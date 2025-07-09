from manager import Manager

if __name__ == "__main__":
    Manager()

# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class Message(BaseModel):
#     message: str
#
# @app.get("/", response_model=Message)
# async def root():
#     return {"message": "Hello World"}
