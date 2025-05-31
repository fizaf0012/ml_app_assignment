# MLflow Tracking Setup Guide

## 1. Start Tracking Server
```bash
# From project root directory:
mlflow ui --backend-store-uri mlruns/ --port 5000
```

## 2. Access the UI
Open in your browser:
```
http://localhost:5000
```

## 3. What You'll See
- Experiment: "Hotel Booking Cancellation"
- Tracked Parameters:
  - n_estimators
  - max_depth
  - random_state
- Tracked Metrics:
  - accuracy
  - precision
  - recall
  - f1-score

## 4. Example Screenshot
![MLflow UI](mlflow_screenshot.png)

## 5. Useful Commands
List all runs:
```bash
mlflow runs list --experiment-id 1
```

Get run details:
```bash
mlflow runs describe --run-id <RUN_ID>
```