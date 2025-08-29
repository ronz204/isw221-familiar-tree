from pydantic import BaseModel, Field

class BetweenPeopleSchema(BaseModel):
  person1: int = Field(gt=0)
  person2: int = Field(gt=0)
