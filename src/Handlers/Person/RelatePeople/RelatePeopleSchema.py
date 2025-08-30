from typing import Optional
from pydantic import BaseModel, Field

class RelatePeopleSchema(BaseModel):
  person_id: int = Field(gt=0)
  mother_id: Optional[int] = None
  father_id: Optional[int] = None
  guardian_id: Optional[int] = None
