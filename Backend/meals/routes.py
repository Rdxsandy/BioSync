from fastapi import APIRouter, Depends, UploadFile, File
from schema.meal_schema import MealCreate
from auth.dependencies import get_current_user
from meals.service import create_meal, get_user_meals, delete_meal
from meals.ml import predict_food

router = APIRouter(prefix="/meals", tags=["Meals"])


# ADD MEAL MANUALLY
@router.post("/")
def add_meal(meal: MealCreate, user=Depends(get_current_user)):
    meal_data = meal.dict()
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


# UPLOAD IMAGE → ML
@router.post("/upload-image")
def upload_meal_image(file: UploadFile = File(...), user=Depends(get_current_user)):

    file_path = f"images/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    food_name, calories = predict_food(file_path)

    meal_data = {
        "user_id": str(user["_id"]),
        "meal_name": food_name,
        "calories": calories
    }

    result = create_meal(meal_data)

    return {
        "food": food_name,
        "calories": calories,
        "data": result
    }