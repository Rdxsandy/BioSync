import requests
import os
import base64

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/google/vit-base-patch16-224"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def analyze_food_image(image_path):

    try:

        with open(image_path, "rb") as f:
            image_bytes = f.read()

        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

        payload = {
            "inputs": image_base64
        }

        response = requests.post(
            API_URL,
            headers=headers,
            json=payload,
            timeout=120
        )

        if response.status_code != 200:
            return {"error": response.text}

        result = response.json()

        food_name = result[0]["label"]

        return {
            "food": food_name,
            "calories": "Estimated by AI",
            "best_time": "Lunch",
            "advice": f"{food_name} can be consumed as part of a balanced diet."
        }

    except Exception as e:
        return {"error": str(e)}