import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException, File
from pydantic import BaseModel
import httpx
from extract_data.extractCSV import ExtractCSV

app = FastAPI()


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        filename = file.filename.lower()
        content = await file.read()

        if filename.endswith(".csv"):
            extractor = ExtractCSV()
            data = extractor.extract_data(content)
            print(f"Data extracted, type: {type(data)}")

            if data is None:
                raise HTTPException(status_code=500, detail="extract_data returned None")
            if isinstance(data, pd.DataFrame):
                data_dict = data.to_dict(orient="records")
            else:
                print("Data is not DataFrame, using as is")
                data_dict = data
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")

        clean_response = await send_to_clean(data_dict)
        return {"data": data_dict, "clean_response": clean_response}
    except Exception as e:
        print(f"Exception in upload: {e}")
        raise HTTPException(status_code=500, detail=f"Error during upload: {str(e)}")


async def send_to_clean(data):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post("http://127.0.0.1:8001/clean", json={"data": data})
            print(f"Response status: {response.status_code}")
            if response.status_code == 200:
                model_response = response.json()

                return model_response
            else:
                print(f"Error response: {response.text}")
        except Exception as e:
            print(f"Error sending to clean service: {e}")
            raise HTTPException(status_code=500, detail="Failed to send data to clean service")