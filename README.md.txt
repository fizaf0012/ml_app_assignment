# Hotel Booking Cancellation Predictor

## Quick Start
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run all services:
```bash
# Terminal 1 - MLflow Tracking
mlflow ui --backend-store-uri mlruns/ --port 5000

# Terminal 2 - Backend API
uvicorn backend.main:app --reload

# Terminal 3 - Frontend
streamlit run frontend/streamlit_app.py
```

## Access Services
- MLflow UI: http://localhost:5000
- FastAPI Docs: http://localhost:8000/docs
- Streamlit App: http://localhost:8501

## Project Structure
```
ml_app_assignment/
├── ml/                      # Model training artifacts
├── backend/                 # FastAPI implementation
├── frontend/                # Streamlit interface
├── mlflow_tracking/         # Tracking documentation
├── requirements.txt
└── README.md
```