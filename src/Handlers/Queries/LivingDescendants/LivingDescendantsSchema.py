from pydantic import BaseModel, Field

class LivingDescendantsSchema(BaseModel):
  person_id: int = Field(gt=0)
