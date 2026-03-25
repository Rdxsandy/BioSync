from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Meal(BaseModel):
    user_id: str
    date: datetime = datetime.utcnow()
    meal_type: str
    food_items: List[str]
    calories: Optional[float]
    image_url: Optional[str]