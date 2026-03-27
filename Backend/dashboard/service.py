from database.db import db
from datetime import datetime, timedelta
from ml.service import predict_risk_from_db

activity_collection = db["activities"]
meals_collection = db["meals"]
health_collection = db["health_scores"]


# -----------------------------
# Latest activity
# -----------------------------
def get_latest_activity(user_id: str):

    activity = activity_collection.find_one(
        {"user_id": user_id},
        sort=[("date", -1)]
    )

    if not activity:
        return {}

    return {
        "steps": activity.get("steps", 0),
        "sleep_hours": activity.get("sleep_hours", 0),
        "exercise_minutes": activity.get("exercise_minutes", 0),
        "water_intake": activity.get("water_intake", 0)
    }


# -----------------------------
# Weekly activity averages
# -----------------------------
def get_weekly_activity_average(user_id: str):

    seven_days_ago = datetime.utcnow() - timedelta(days=7)

    weekly_activities = list(
        activity_collection.find({
            "user_id": user_id,
            "date": {"$gte": seven_days_ago}
        })
    )

    if not weekly_activities:
        return {
            "average_steps_week": 0,
            "average_sleep_week": 0,
            "average_exercise_week": 0
        }

    avg_steps = sum(a.get("steps", 0) for a in weekly_activities) / len(weekly_activities)
    avg_sleep = sum(a.get("sleep_hours", 0) for a in weekly_activities) / len(weekly_activities)
    avg_exercise = sum(a.get("exercise_minutes", 0) for a in weekly_activities) / len(weekly_activities)

    return {
        "average_steps_week": round(avg_steps, 2),
        "average_sleep_week": round(avg_sleep, 2),
        "average_exercise_week": round(avg_exercise, 2)
    }


# -----------------------------
# Weekly activity trends (for charts)
# -----------------------------
def get_weekly_activity_trends(user_id: str):

    seven_days_ago = datetime.utcnow() - timedelta(days=7)

    activities = activity_collection.find(
        {
            "user_id": user_id,
            "date": {"$gte": seven_days_ago}
        }
    ).sort("date", 1)

    steps_trend = []
    sleep_trend = []
    exercise_trend = []

    for activity in activities:

        date_str = activity["date"].strftime("%Y-%m-%d")

        steps_trend.append({
            "date": date_str,
            "steps": activity.get("steps", 0)
        })

        sleep_trend.append({
            "date": date_str,
            "sleep_hours": activity.get("sleep_hours", 0)
        })

        exercise_trend.append({
            "date": date_str,
            "exercise_minutes": activity.get("exercise_minutes", 0)
        })

    return {
        "weekly_steps_trend": steps_trend,
        "weekly_sleep_trend": sleep_trend,
        "weekly_exercise_trend": exercise_trend
    }


# -----------------------------
# Calories today
# -----------------------------
def get_calories_today(user_id: str):

    today_start = datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    meals_today = list(
        meals_collection.find({
            "user_id": user_id,
            "date": {"$gte": today_start}
        })
    )

    return sum(meal.get("calories", 0) for meal in meals_today)


# -----------------------------
# Weekly health trend
# -----------------------------
def get_weekly_health_trend(user_id: str):

    seven_days_ago = datetime.utcnow() - timedelta(days=7)

    health_data = health_collection.find({
        "user_id": user_id,
        "date": {"$gte": seven_days_ago}
    }).sort("date", 1)

    weekly_trend = []

    for record in health_data:
        weekly_trend.append({
            "date": record["date"].strftime("%Y-%m-%d"),
            "score": record["total_score"]
        })

    return weekly_trend


# -----------------------------
# Dashboard summary
# -----------------------------
def get_dashboard_summary(user_id: str):

    return {
        "activity_today": get_latest_activity(user_id),
        "weekly_activity_average": get_weekly_activity_average(user_id),
        "activity_trends": get_weekly_activity_trends(user_id),
        "calories_today": get_calories_today(user_id),
        "weekly_health_trend": get_weekly_health_trend(user_id),
        "risk_level": predict_risk_from_db(user_id)
    }