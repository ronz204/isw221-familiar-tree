from pydantic import BaseModel, Field

class WidowedPersonSchema(BaseModel):
  person_id: int = Field(gt=0)
