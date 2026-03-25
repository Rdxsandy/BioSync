import joblib
import os

# Get current directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load trained model
model = joblib.load(os.path.join(BASE_DIR, "risk_prediction_model.pkl"))

# Load label encoder
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))


def predict_risk(sleep_hours, exercise_minutes, steps, calories):

    features = [[sleep_hours, exercise_minutes, steps, calories]]

    prediction = model.predict(features)

    risk_level = encoder.inverse_transform(prediction)

    return risk_level[0]