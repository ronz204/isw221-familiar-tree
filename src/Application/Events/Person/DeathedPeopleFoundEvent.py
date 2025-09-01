from typing import Dict, Any
from Application.Events.Event import Event

class DeathedPeopleFoundEvent(Event):
  name: str = "deathed_people_found"
  label: str = "Deceased People Found Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
