from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Activity(BaseModel):
    user_id: str
    date: datetime = Field(default_factory=datetime.utcnow)
    steps: Optional[int]
    sleep_hours: Optional[float]
    water_intake: Optional[float]
    exercise_minutes: Optional[int]