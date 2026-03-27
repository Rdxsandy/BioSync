from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user
from health.service import calculate_health_score, get_weekly_health
from schema.health_schema import HealthScore

router = APIRouter(prefix="/health", tags=["Health"])


# Get today's health score
@router.get("/today", response_model=HealthScore)
def get_today_health(user=Depends(get_current_user)):

    user_id = str(user["_id"])

    score = calculate_health_score(user_id)

    if not score:
        return {
            "sleep_score": 0,
            "activity_score": 0,
            "nutrition_score": 0,
            "total_score": 0
        }

    return {
        "sleep_score": score["sleep_score"],
        "activity_score": score["activity_score"],
        "nutrition_score": score["nutrition_score"],
        "total_score": score["total_score"]
    }


# Get weekly health scores
@router.get("/weekly")
def get_weekly_health_score(user=Depends(get_current_user)):

    user_id = str(user["_id"])

    data = get_weekly_health(user_id)

    return data