from pydantic import BaseModel
from datetime import datetime

class Health(BaseModel):
    user_id: str
    date: datetime = datetime.utcnow()
    sleep_score: float
    activity_score: float
    nutrition_score: float
    total_score: float