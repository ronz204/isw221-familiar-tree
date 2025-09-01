from typing import Dict, Any
from Application.Events.Event import Event

class DescendantsFoundAliveEvent(Event):
  name: str = "descendants_found_alive"
  label: str = "Descendants Found Alive Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
