from models.meals import meal_collection
from bson import ObjectId


# CREATE MEAL
def create_meal(meal_data):
    result = meal_collection.insert_one(meal_data)
    meal_data["_id"] = str(result.inserted_id)
    return meal_data


# GET USER MEALS
def get_user_meals(user_id):
    meals = []

    for meal in meal_collection.find({"user_id": user_id}):
        meal["_id"] = str(meal["_id"])
        meals.append(meal)

    return meals


# DELETE MEAL
def delete_meal(meal_id, user_id):
    result = meal_collection.delete_one({
        "_id": ObjectId(meal_id),
        "user_id": user_id
    })

    return result.deleted_count