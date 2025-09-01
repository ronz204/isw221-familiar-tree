from pydantic import BaseModel, Field

class MaternalAncestorsSchema(BaseModel):
  person_id: int = Field(gt=0)
