#!/bin/bash

# יוצרים רשת דוקר
docker network create bayes-net

# בונים את האימג'ים
docker build -t model-service ./model
docker build -t predictor-service ./predictor

# מריצים את השרת של המודל ברקע
docker run -d --name model-service --network bayes-net model-service

# מחכים 10 שניות כדי שהמודל יסיים את ההקמה
echo "Waiting 10 seconds for model-service to start..."
sleep 10

# מריצים את השרת של הפרדיקטור, עם חשיפת פורט
docker run -d -p 8001:8000 --name predictor-service --network bayes-net predictor-service

echo "All services started successfully."
