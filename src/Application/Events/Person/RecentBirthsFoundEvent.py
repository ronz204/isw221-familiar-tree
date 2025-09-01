from typing import Dict, Any
from Application.Events.Event import Event

class RecentBirthsFoundEvent(Event):
  name: str = "recent_births_found"
  label: str = "Recent Births Found Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
