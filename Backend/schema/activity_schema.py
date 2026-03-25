from pydantic import BaseModel
from typing import Optional

class ActivityCreate(BaseModel):
    steps: Optional[int]
    sleep_hours: Optional[float]
    water_intake: Optional[float]
    exercise_minutes: Optional[int]