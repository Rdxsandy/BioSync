from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Activity(BaseModel):
    user_id: str
    date: datetime = datetime.utcnow()
    steps: Optional[int]
    sleep_hours: Optional[float]
    water_intake: Optional[float]
    exercise_minutes: Optional[int]