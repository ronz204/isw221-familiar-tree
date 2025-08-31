from typing import Dict, Any
from Application.Events.Event import Event

class PersonBornEvent(Event):
  name: str = "person_born"
  label: str = "Person Born Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
