from typing import Optional
from pydantic import BaseModel, Field

class RelatePeopleSchema(BaseModel):
  person_id: int = Field(gt=0)
  guard_id: Optional[int] = None
  mother_id: Optional[int] = None
  father_id: Optional[int] = None
