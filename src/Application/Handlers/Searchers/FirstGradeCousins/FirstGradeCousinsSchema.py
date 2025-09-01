from pydantic import BaseModel, Field

class FirstGradeCousinsSchema(BaseModel):
  person_id: int = Field(gt=0)
