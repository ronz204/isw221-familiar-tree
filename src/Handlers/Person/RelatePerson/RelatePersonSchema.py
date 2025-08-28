from pydantic import BaseModel, Field

class RelatePersonSchema(BaseModel):
  year: int = Field(gt=0)
  man_id: int = Field(gt=0)
  woman_id: int = Field(gt=0)
