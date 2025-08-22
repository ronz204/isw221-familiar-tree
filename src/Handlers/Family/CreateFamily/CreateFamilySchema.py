from pydantic import BaseModel, Field

class CreateFamilySchema(BaseModel):
  name: str = Field(min_length=2, max_length=20)
