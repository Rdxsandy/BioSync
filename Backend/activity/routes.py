from fastapi import APIRouter, Depends
from schema.activity_schema import ActivityCreate
from activity.service import predict_future_activity
from auth.dependencies import get_current_user
from activity.service import (
    create_activity,
    get_user_activities,
    update_activity,
    delete_activity
)

router = APIRouter(prefix="/activity", tags=["Activity"])

@router.get("/predict-future")
def predict_activity(user=Depends(get_current_user)):

    result = predict_future_activity(str(user["_id"]))

    return result


# ADD ACTIVITY
@router.post("/")
def add_activity(activity: ActivityCreate, user=Depends(get_current_user)):

    activity_data = activity.dict()
    activity_data["user_id"] = str(user["_id"])

    result = create_activity(activity_data)

    return {
        "message": "Activity added successfully",
        "data": result
    }


# GET USER ACTIVITIES
@router.get("/")
def get_activities(user=Depends(get_current_user)):

    activities = get_user_activities(str(user["_id"]))

    return activities


# UPDATE ACTIVITY
@router.put("/{activity_id}")
def update_user_activity(
    activity_id: str,
    activity: ActivityCreate,
    user=Depends(get_current_user)
):

    activity_data = activity.dict()

    updated = update_activity(
        activity_id,
        activity_data,
        str(user["_id"])
    )

    if updated:
        return {"message": "Activity updated successfully"}

    return {"message": "Activity not found"}


# DELETE ACTIVITY
@router.delete("/{activity_id}")
def remove_activity(activity_id: str, user=Depends(get_current_user)):

    deleted = delete_activity(activity_id, str(user["_id"]))

    if deleted:
        return {"message": "Activity deleted successfully"}

    return {"message": "Activity not found"}