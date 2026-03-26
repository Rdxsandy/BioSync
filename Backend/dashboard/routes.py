from fastapi import APIRouter, Depends
from dashboard.service import get_dashboard_summary
from auth.dependencies import get_current_user

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def dashboard_summary(current_user=Depends(get_current_user)):

    user_id = str(current_user["_id"])

    return get_dashboard_summary(user_id)