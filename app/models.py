from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional

# Item model
class Item(BaseModel):
    name: str
    email: EmailStr
    item_name: str
    quantity: int
    expiry_date: datetime
    inserted_data: Optional[datetime] = None

# ClockIn model
class ClockIn(BaseModel):
    email: EmailStr
    location: str
    inserted_data: Optional[datetime] = None
