from typing import Dict, Any
from Application.Events.Event import Event

class MaternalAncestorsFoundEvent(Event):
  name: str = "maternal_ancestors_found"
  label: str = "Maternal Ancestors Found Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
