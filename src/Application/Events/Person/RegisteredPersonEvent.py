from typing import Dict, Any
from Application.Events.Event import Event

class RegisteredPersonEvent(Event):
  name: str = "registered_person"
  label: str = "Person Registered Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
