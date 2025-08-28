from pydantic import BaseModel, Field

class RelatePersonSchema(BaseModel):
  year: int = Field(gt=0)
  person1_id: int = Field(gt=0)
  person2_id: int = Field(gt=0)
