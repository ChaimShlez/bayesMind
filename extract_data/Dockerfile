FROM python:3.12-slim

WORKDIR /app

COPY extract_data/ /app/extract_data


COPY base/ /app/base/


COPY extract_data/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

ENV PYTHONPATH=/app

CMD ["uvicorn", "extract_data.main:app", "--host", "0.0.0.0", "--port", "8000"]
