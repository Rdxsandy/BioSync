import numpy as np
import joblib
import os
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "lstm_activity_model.h5")
SCALER_PATH = os.path.join(BASE_DIR, "activity_scaler.pkl")

model = load_model(MODEL_PATH, compile=False)
scaler = joblib.load(SCALER_PATH)


def predict_next_7_days(activity_data):

    data = np.array(activity_data)

    scaled = scaler.transform(data)

    sequence = scaled.reshape(1, 7, 3)

    predictions = []
    current_sequence = sequence.copy()

    # averages for sleep & exercise
    avg_sleep = np.mean(data[:, 1])
    avg_exercise = np.mean(data[:, 2])

    for _ in range(7):

        pred = model.predict(current_sequence, verbose=0)

        step_prediction = float(pred[0][0])

        new_row = np.array([[step_prediction, avg_sleep, avg_exercise]])

        new_row_scaled = scaler.transform(new_row)

        new_step = new_row_scaled.reshape(1, 1, 3)

        current_sequence = np.concatenate(
            (current_sequence[:, 1:, :], new_step),
            axis=1
        )

        predictions.append([step_prediction, avg_sleep, avg_exercise])

    predictions = np.array(predictions)

    future = scaler.inverse_transform(predictions)

    future[:, 0] = np.maximum(future[:, 0], 0)

    return future.tolist()