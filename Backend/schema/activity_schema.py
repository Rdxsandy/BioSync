from pydantic import BaseModel, Field
from typing import Optional


class ActivityCreate(BaseModel):
    steps: Optional[int] = Field(default=None, ge=0)
    sleep_hours: Optional[float] = Field(default=None, ge=0)
    water_intake: Optional[float] = Field(default=None, ge=0)
    exercise_minutes: Optional[int] = Field(default=None, ge=0)