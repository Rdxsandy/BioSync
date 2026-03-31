from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/health", tags=["Health"])

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------------
# AI Daily Health Facts
# -----------------------------
@router.get("/daily-fact")
def get_daily_health_fact(user=Depends(get_current_user)):

    try:
        response = model.generate_content(
            "Generate 10 short health tips for maintaining a healthy lifestyle."
        )

        facts = response.text

    except Exception as e:
        print("Gemini Error:", e)
        facts = "AI service temporarily unavailable."

    return {
        "health_fact": facts
    }