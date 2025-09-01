from pydantic import BaseModel, Field

class DisplayTimelineSchema(BaseModel):
  person_id: int = Field(gt=0)
