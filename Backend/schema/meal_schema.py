from pydantic import BaseModel
from typing import List, Optional

class MealCreate(BaseModel):
    meal_type: str
    food_items: List[str]
    calories: Optional[float]
    image_url: Optional[str]