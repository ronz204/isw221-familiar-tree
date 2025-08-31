from datetime import date
from pydantic import BaseModel, Field

class CouplePersonSchema(BaseModel):
  timestamp: date
  man_id: int = Field(gt=0)
  woman_id: int = Field(gt=0)
