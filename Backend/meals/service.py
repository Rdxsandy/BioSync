from database.db import db
from bson import ObjectId
from datetime import datetime

meal_collection = db["meals"]


# CREATE MEAL (store meal with AI insights)
def create_meal(meal_data):

    meal_data["created_at"] = datetime.utcnow()

    result = meal_collection.insert_one(meal_data)

    meal_data["_id"] = str(result.inserted_id)

    return meal_data


# GET USER MEALS
def get_user_meals(user_id):

    meals = []

    for meal in meal_collection.find({"user_id": user_id}).sort("created_at", -1):

        meal["_id"] = str(meal["_id"])

        meals.append(meal)

    return meals


# GET SINGLE MEAL
def get_meal(meal_id, user_id):

    meal = meal_collection.find_one({
        "_id": ObjectId(meal_id),
        "user_id": user_id
    })

    if meal:
        meal["_id"] = str(meal["_id"])

    return meal


# DELETE MEAL
def delete_meal(meal_id, user_id):

    result = meal_collection.delete_one({
        "_id": ObjectId(meal_id),
        "user_id": user_id
    })

    return result.deleted_count