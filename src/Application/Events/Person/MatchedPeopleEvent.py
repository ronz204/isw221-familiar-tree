from typing import Dict, Any
from Application.Events.Event import Event

class MatchedPeopleEvent(Event):
  name: str = "matched_people"
  label: str = "Matched People Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
