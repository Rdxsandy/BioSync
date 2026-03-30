import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API KEY:", api_key)

# Configure Gemini
genai.configure(api_key=api_key)

try:
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(
        "Generate 5 short health tips."
    )

    print("\nGemini Response:")
    print(response.text)

except Exception as e:
    print("\nGemini Error:")
    print(e)