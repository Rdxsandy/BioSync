from fastapi import APIRouter
from ml.service import predict_risk

router = APIRouter(prefix="/ml", tags=["ML"])


@router.get("/risk-score")
def get_risk_score(
    sleep_hours: float,
    exercise_minutes: float,
    steps: int,
    calories: float
):

    risk = predict_risk(
        sleep_hours,
        exercise_minutes,
        steps,
        calories
    )

    return {
        "risk_level": risk
    }