FROM python:3.12-slim

WORKDIR /app

COPY predictor/ /app/predictor/
COPY trainer/ /app/trainer/
COPY trainer/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONPATH=/app

CMD ["uvicorn", "trainer.main:app", "--host", "0.0.0.0", "--port", "8002"]
