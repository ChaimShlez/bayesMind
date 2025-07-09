from predictor.naiveBayesPredictor import NaiveBayesPredictor

def main():
    data_to_predict = {
        'age': 'senior',
        'income': 'high',
        'student': 'yes',
        'credit_rating': 'excellent'
    }

    predictor = NaiveBayesPredictor()
    prediction = predictor.Predictor(data_to_predict)
    print("pred:", prediction)

if __name__ == "__main__":
    main()
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
