import google.generativeai as genai
import os
import PIL.Image
import json

def analyze_food_image(image_path):
    try:
        # Load Gemini Key that we just set in Render
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            return {"error": "GEMINI_API_KEY is missing"}
            
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        
        img = PIL.Image.open(image_path)
        
        prompt = """
        Analyze this food image. Identify the food, estimate the calories, suggest the best time to eat it, and provide a short piece of dietary advice.
        You MUST respond ONLY with a valid JSON object in this exact format:
        {
            "food": "Name of the food",
            "calories": "e.g. 350 kcal",
            "best_time": "e.g. Breakfast",
            "advice": "short dietary advice"
        }
        Do not add markdown formatting or backticks around the json.
        """
        
        response = model.generate_content([prompt, img])
        
        # Clean response string to ensure it parses as JSON
        text = response.text.strip()
        if text.startswith('```json'):
            text = text[7:]
        if text.startswith('```'):
            text = text[3:]
        if text.endswith('```'):
            text = text[:-3]
            
        result = json.loads(text.strip())
        
        return {
            "food": result.get("food", "Unknown Food"),
            "calories": result.get("calories", "Unknown"),
            "best_time": result.get("best_time", "Anytime"),
            "advice": result.get("advice", "Consume as part of a balanced diet.")
        }

    except Exception as e:
        return {"error": f"AI Error: {str(e)}"}