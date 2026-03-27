from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user
from ml.service import predict_risk_from_db

router = APIRouter(prefix="/ml", tags=["ML"])


@router.get("/risk-score")
def get_risk_score(user=Depends(get_current_user)):

    user_id = str(user["_id"])

    risk = predict_risk_from_db(user_id)

    return {
        "risk_level": risk
    }