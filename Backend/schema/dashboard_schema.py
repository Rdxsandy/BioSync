from pydantic import BaseModel
from typing import List


class ActivityToday(BaseModel):
    steps: int
    sleep_hours: float
    exercise_minutes: int
    water_intake: float


class WeeklyHealth(BaseModel):
    date: str
    score: float


class DashboardSummary(BaseModel):
    activity_today: ActivityToday
    calories_today: int
    weekly_health_trend: List[WeeklyHealth]
    risk_level: str