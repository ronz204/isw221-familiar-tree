from typing import Dict, Any
from Application.Events.Event import Event

class RelatePeopleEvent(Event):
  name: str = "relate_people"
  label: str = "Relate People Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
