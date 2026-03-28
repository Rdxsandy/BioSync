import numpy as np
import joblib
import os
from tensorflow.keras.models import load_model

# Get directory of this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model paths
MODEL_PATH = os.path.join(BASE_DIR, "lstm_activity_model.h5")
SCALER_PATH = os.path.join(BASE_DIR, "activity_scaler.pkl")

# Load model and scaler
model = load_model(MODEL_PATH, compile=False)
scaler = joblib.load(SCALER_PATH)


def predict_next_7_days(activity_data):

    data = np.array(activity_data)

    scaled = scaler.transform(data)

    sequence = scaled.reshape(1, 7, 3)

    predictions = []
    current_sequence = sequence.copy()

    for _ in range(7):

        pred = model.predict(current_sequence, verbose=0)

        step_prediction = pred[0][0]

        predictions.append(step_prediction)

        new_row = np.array([[step_prediction, 0, 0]])

        new_row_scaled = scaler.transform(new_row)

        new_step = new_row_scaled.reshape(1, 1, 3)

        current_sequence = np.concatenate(
            (current_sequence[:, 1:, :], new_step),
            axis=1
        )

    # Convert predictions back to original scale
    predictions = np.array(predictions).reshape(-1, 1)

    fake_rows = np.hstack((predictions, np.zeros((len(predictions), 2))))

    future = scaler.inverse_transform(fake_rows)

    steps = future[:, 0]

    steps = np.maximum(steps, 0)
    return steps.tolist()