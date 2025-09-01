from typing import Dict, Any
from Application.Events.Event import Event

class RelativesFoundEvent(Event):
  name: str = "relatives_found"
  label: str = "Relatives Found Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
