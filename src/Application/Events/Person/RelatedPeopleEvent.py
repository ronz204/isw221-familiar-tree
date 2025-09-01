from typing import Dict, Any
from Application.Events.Event import Event

class RelatedPeopleEvent(Event):
  name: str = "related_people"
  label: str = "Related People Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
