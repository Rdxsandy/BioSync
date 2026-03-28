from database.db import db
from datetime import datetime, timedelta
from ml.service import predict_risk_from_db

activity_collection = db["activities"]
meals_collection = db["meals"]
health_collection = db["health_scores"]


# -----------------------------
# Today's activity
# -----------------------------
def get_today_activity(user_id: str):

    today_start = datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    today_end = today_start + timedelta(days=1)

    activity = activity_collection.find_one({
        "user_id": user_id,
        "date": {
            "$gte": today_start,
            "$lt": today_end
        }
    })

    if not activity:
        return {
            "steps": 0,
            "sleep_hours": 0,
            "exercise_minutes": 0,
            "water_intake": 0
        }

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
# Weekly activity trends
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

        date_value = activity.get("date")

        if date_value:
            date_str = date_value.strftime("%Y-%m-%d")
        else:
            date_str = "unknown"

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

    today_end = today_start + timedelta(days=1)

    meals_today = list(
        meals_collection.find({
            "user_id": user_id,
            "created_at": {
                "$gte": today_start,
                "$lt": today_end
            }
        })
    )

    total_calories = 0

    for meal in meals_today:
        value = meal.get("calories", 0)

        try:
            total_calories += float(value)
        except (TypeError, ValueError):
            # ignore invalid values like "Estimated by AI"
            total_calories += 0

    return round(total_calories, 2)

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

        date_value = record.get("date")

        if date_value:
            date_str = date_value.strftime("%Y-%m-%d")
        else:
            date_str = "unknown"

        weekly_trend.append({
            "date": date_str,
            "score": record.get("total_score", 0)
        })

    return weekly_trend


# -----------------------------
# Calculate health score
# -----------------------------
def calculate_health_score(weekly_avg):

    steps = weekly_avg["average_steps_week"]
    sleep = weekly_avg["average_sleep_week"]
    exercise = weekly_avg["average_exercise_week"]

    steps_score = min(steps / 10000, 1) * 40
    sleep_score = min(sleep / 8, 1) * 30
    exercise_score = min(exercise / 30, 1) * 30

    total_score = steps_score + sleep_score + exercise_score

    return round(total_score, 2)


# -----------------------------
# Dashboard summary
# -----------------------------
def get_dashboard_summary(user_id: str):

    today_activity = get_today_activity(user_id)

    weekly_avg = get_weekly_activity_average(user_id)

    health_score = calculate_health_score(weekly_avg)

    return {
        "activity_today": today_activity,
        "weekly_activity_average": weekly_avg,
        "activity_trends": get_weekly_activity_trends(user_id),
        "calories_today": get_calories_today(user_id),
        "weekly_health_trend": get_weekly_health_trend(user_id),
        "health_score": health_score,
        "risk_level": predict_risk_from_db(user_id)
    }