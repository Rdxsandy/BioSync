from pydantic import BaseModel

class HealthScore(BaseModel):
    sleep_score: float
    activity_score: float
    nutrition_score: float
    total_score: float