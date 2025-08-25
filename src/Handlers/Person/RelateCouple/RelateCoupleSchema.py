from pydantic import BaseModel, Field

class RelateCoupleSchema(BaseModel):
  person1_id: int = Field(gt=0)
  person2_id: int = Field(gt=0)
