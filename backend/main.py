from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
import numpy as np

app = FastAPI()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../ml/model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Input schema
class BookingFeatures(BaseModel):
    lead_time: int
    adults: int
    children: int = 0
    booking_changes: int = 0
    required_car_parking_spaces: int = 0

@app.post("/predict")
async def predict(features: BookingFeatures):
    features_array = np.array([
        features.lead_time,
        features.adults,
        features.children,
        features.booking_changes,
        features.required_car_parking_spaces
    ]).reshape(1, -1)
    
    prediction = model.predict(features_array)
    probability = model.predict_proba(features_array)[0][1]
    
    return {
        "will_cancel": bool(prediction[0]),
        "cancellation_probability": float(probability)
    }

@app.get("/")
async def health_check():
    return {"status": "healthy"}