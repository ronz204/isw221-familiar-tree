from datetime import date
from typing import Optional
from pydantic import BaseModel, Field

class RegisterPersonSchema(BaseModel):
  name: str = Field(min_length=2, max_length=40)
  cedula: str = Field(min_length=9, max_length=9)
  gender: str = Field(pattern="^(M|F)$")
  province: str = Field(min_length=2, max_length=100)
  emotional: Optional[int] = Field(default=100, ge=0, le=100)

  age: int = Field(ge=0, le=100)
  birthdate: date
  deathdate: Optional[date] = None

  mother_id: Optional[int] = None
  father_id: Optional[int] = None
  guardian_id: Optional[int] = None
