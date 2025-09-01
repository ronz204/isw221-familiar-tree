from typing import Dict, Any
from Application.Events.Event import Event

class CousinsFoundEvent(Event):
  name: str = "cousins_found"
  label: str = "Cousins Found Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
