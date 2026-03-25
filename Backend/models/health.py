from pydantic import BaseModel, Field
from datetime import datetime


class Health(BaseModel):
    user_id: str
    date: datetime = Field(default_factory=datetime.utcnow)
    sleep_score: float
    activity_score: float
    nutrition_score: float
    total_score: float