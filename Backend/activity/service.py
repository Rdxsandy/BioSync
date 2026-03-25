from database.db import db
from bson import ObjectId

activity_collection = db["activities"]


# CREATE ACTIVITY
def create_activity(activity_data):
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