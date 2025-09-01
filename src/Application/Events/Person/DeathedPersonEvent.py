from typing import Dict, Any
from Application.Events.Event import Event

class DeathedPersonEvent(Event):
  name: str = "deathed_person"
  label: str = "Deathed Person Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
