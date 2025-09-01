from typing import Dict, Any
from Application.Events.Event import Event

class YearsCelebratedEvent(Event):
  name: str = "years_celebrated"
  label: str = "Years Celebrated Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
