from typing import Dict, Any
from Application.Events.Event import Event

class ChildrenTogetherFoundEvent(Event):
  name: str = "children_together_found"
  label: str = "Children Together Found Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
