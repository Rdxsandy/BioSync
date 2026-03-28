from database.db import db
from bson import ObjectId
from datetime import datetime

from ml.predict import predict_next_7_days

activity_collection = db["activities"]


# CREATE ACTIVITY
def create_activity(activity_data: dict):

    today_start = datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    existing = activity_collection.find_one({
        "user_id": activity_data["user_id"],
        "date": {"$gte": today_start}
    })

    # If activity exists for today → update
    if existing:

        activity_collection.update_one(
            {"_id": existing["_id"]},
            {"$set": activity_data}
        )

        activity_data["_id"] = str(existing["_id"])
        return activity_data

    # Otherwise insert new record
    activity_data["date"] = datetime.utcnow()

    result = activity_collection.insert_one(activity_data)

    activity_data["_id"] = str(result.inserted_id)

    return activity_data


# GET ALL ACTIVITIES FOR USER
def get_user_activities(user_id):

    activities = []

    for activity in activity_collection.find({"user_id": user_id}):
        activity["_id"] = str(activity["_id"])
        activities.append(activity)

    return activities


# UPDATE ACTIVITY
def update_activity(activity_id, activity_data, user_id):

    result = activity_collection.update_one(
        {
            "_id": ObjectId(activity_id),
            "user_id": user_id
        },
        {
            "$set": activity_data
        }
    )

    return result.modified_count


# DELETE ACTIVITY
def delete_activity(activity_id, user_id):

    result = activity_collection.delete_one(
        {
            "_id": ObjectId(activity_id),
            "user_id": user_id
        }
    )

    return result.deleted_count


# AI ACTIVITY PREDICTION
def predict_future_activity(user_id):

    activities = list(
        activity_collection
        .find({"user_id": user_id})
        .sort("date", -1)
        .limit(7)
    )

    # Ensure we have enough data
    if len(activities) < 7:
        return {
            "error": "Not enough activity data (minimum 7 days required)"
        }

    activities.reverse()

    sequence = []

    for activity in activities:

        steps = activity.get("steps", 0)
        sleep = activity.get("sleep_hours", 0)
        exercise = activity.get("exercise_minutes", 0)

        sequence.append([
            steps,
            sleep,
            exercise
        ])

    future_predictions = predict_next_7_days(sequence)

    return {
        "past_7_days": sequence,
        "future_7_days": future_predictions
    }