from fastapi import APIRouter, Depends, UploadFile, File
from schema.meal_schema import MealCreate
from auth.dependencies import get_current_user
from meals.service import create_meal, get_user_meals, delete_meal
from ml.ai_service import analyze_food_image

import os
import shutil
import uuid

router = APIRouter(prefix="/meals", tags=["Meals"])


# AI MEAL ANALYSIS
@router.post("/analyze")
async def analyze_meal(
    file: UploadFile = File(...),
    user=Depends(get_current_user)
):

    os.makedirs("uploads", exist_ok=True)

    # Generate unique filename
    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = f"uploads/{filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run AI model
    result = analyze_food_image(file_path)

    if "error" in result:
        return {
            "message": "AI analysis failed",
            "error": result["error"]
        }

    meal_data = {
        "user_id": str(user["_id"]),
        "image_url": file_path,
        "food_name": result["food"],
        "calories": result["calories"],
        "best_time": result["best_time"],
        "advice": result["advice"]
    }

    saved_meal = create_meal(meal_data)

    return {
        "message": "Meal analyzed successfully",
        "data": saved_meal
    }


# ADD MEAL MANUALLY
@router.post("/")
def add_meal(meal: MealCreate, user=Depends(get_current_user)):

    meal_data = meal.dict(exclude_none=True)
    meal_data["user_id"] = str(user["_id"])

    result = create_meal(meal_data)

    return {
        "message": "Meal added successfully",
        "data": result
    }


# GET USER MEALS
@router.get("/")
def get_meals(user=Depends(get_current_user)):

    return get_user_meals(str(user["_id"]))


# DELETE MEAL
@router.delete("/{meal_id}")
def remove_meal(meal_id: str, user=Depends(get_current_user)):

    deleted = delete_meal(meal_id, str(user["_id"]))

    if deleted:
        return {"message": "Meal deleted successfully"}

    return {"message": "Meal not found"}