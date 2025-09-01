from typing import Dict, Any
from Application.Events.Event import Event

class WidowedPersonEvent(Event):
  name: str = "widowed_person"
  label: str = "Widowed Person Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
