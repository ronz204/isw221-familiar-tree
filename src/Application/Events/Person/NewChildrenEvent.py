from typing import Dict, Any
from Application.Events.Event import Event

class NewChildrenEvent(Event):
  name: str = "new_children"
  label: str = "New Children Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
