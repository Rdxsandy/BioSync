import joblib
import os
import numpy as np
from database.db import db

# Get path of current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load ML model and encoder
model = joblib.load(os.path.join(BASE_DIR, "risk_prediction_model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))

activity_collection = db["activities"]
meal_collection = db["meals"]


def safe_float(value, default=0):
    """
    Convert values to float safely.
    Handles strings like 'Estimated by AI'.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def predict_risk_from_db(user_id):

    # Get last 7 activity records
    activities = list(
        activity_collection.find({"user_id": user_id})
        .sort("date", -1)
        .limit(7)
    )

    # Get last 7 meal records
    meals = list(
        meal_collection.find({"user_id": user_id})
        .sort("date", -1)
        .limit(7)
    )

    if not activities:
        return "Not enough activity data"

    # Compute averages safely
    sleep_hours = np.mean([
        safe_float(a.get("sleep_hours", 0)) for a in activities
    ])

    exercise_minutes = np.mean([
        safe_float(a.get("exercise_minutes", 0)) for a in activities
    ])

    steps = np.mean([
        safe_float(a.get("steps", 0)) for a in activities
    ])

    # Handle meals calories safely
    if meals:
        calories_list = [
            safe_float(m.get("calories", 2000), 2000) for m in meals
        ]
        calories = np.mean(calories_list)
    else:
        calories = 2000

    # Prepare model input
    features = [[sleep_hours, exercise_minutes, steps, calories]]

    prediction = model.predict(features)

    risk_level = encoder.inverse_transform(prediction)

    return risk_level[0]