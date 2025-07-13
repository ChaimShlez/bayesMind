from typing import Any, Dict, List

import httpx
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from cleanAndSplitData.splitData import SplitData

app = FastAPI()


class InputData(BaseModel):
    data: List[Dict[str, Any]]





@app.post("/clean")
async def clean(input: InputData):
    try:
        df = pd.DataFrame(input.data)
        # print(f"DataFrame shape: {df.shape}")
        split = SplitData()
        label = split.extract_label(df)
        df_data, x_test, y_test = split.split_from_test_modal(df)
        print(f"Label distribution: {label}")
        print(df_data)
        print(x_test)
        print(y_test)
        await send_to_trainer(df_data,label)

        await send_to_evaluator(x_test,y_test)
        # return {
        #     "data": {
        #         "df_data": df_data.to_dict(orient="records"),
        #         "x_test": x_test.to_dict(orient="records"),
        #         "y_test": y_test.tolist()
        #     },
        #     "label": label
        # }
    except Exception as e:
        print(f"Error in clean function: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")



async def send_to_trainer(df_data, label):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://127.0.0.1:8002/train",
                json={
                    "features": df_data.to_dict(orient="records"),
                    "labels": label
                }

            )
            print(f"Response status: {response.status_code}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error response: {response.text}")
        except Exception as e:
            print(f"Error sending to train service: {e}")
            raise HTTPException(status_code=500, detail="Failed to send data to train service")



async def send_to_evaluator(x_test, y_test):
    async with httpx.AsyncClient() as client:
        try:
            response=await client.post("http://127.0.0.1:8002/evaluator",
                json={"features": x_test.to_dict(orient="records"),  "labels": y_test.tolist()})

            print(f"Response status: {response.status_code}")
            if response.status_code == 200:
               return response.json()
            else:
              print(f"Error response: {response.text}")
        except Exception as e:
          print(f"Error sending to train service: {e}")
          raise HTTPException(status_code=500, detail="Failed to send data to evaluator service")