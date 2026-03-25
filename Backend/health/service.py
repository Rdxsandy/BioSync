from database.db import db
from datetime import datetime, timedelta

activity_collection = db["activities"]
meals_collection = db["meals"]
health_collection = db["health_scores"]


def calculate_health_score(user_id: str):

    # get latest activity
    activity = activity_collection.find_one(
        {"user_id": user_id},
        sort=[("date", -1)]
    )

    if not activity:
        return None

    sleep_hours = activity.get("sleep_hours", 0)
    exercise_minutes = activity.get("exercise_minutes", 0)

    # sleep score
    sleep_score = min((sleep_hours / 8) * 100, 100)

    # activity score
    activity_score = min((exercise_minutes / 60) * 100, 100)

    # nutrition score based on meals count
    meal_count = meals_collection.count_documents({"user_id": user_id})

    nutrition_score = min(meal_count * 25, 100)

    total_score = (sleep_score + activity_score + nutrition_score) / 3

    result = {
        "user_id": user_id,
        "date": datetime.utcnow(),
        "sleep_score": round(sleep_score, 2),
        "activity_score": round(activity_score, 2),
        "nutrition_score": round(nutrition_score, 2),
        "total_score": round(total_score, 2)
    }

    # store health score (important for weekly analytics and AI later)
    health_collection.insert_one(result)

    return result


def get_weekly_health(user_id: str):

    today = datetime.utcnow()
    seven_days_ago = today - timedelta(days=7)

    health_data = health_collection.find({
        "user_id": user_id,
        "date": {"$gte": seven_days_ago}
    }).sort("date", 1)

    weekly_scores = []

    for record in health_data:
        weekly_scores.append({
            "date": record["date"].strftime("%Y-%m-%d"),
            "sleep_score": record["sleep_score"],
            "activity_score": record["activity_score"],
            "nutrition_score": record["nutrition_score"],
            "total_score": record["total_score"]
        })

    return weekly_scores