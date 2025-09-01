from typing import Dict, Any
from Application.Events.Event import Event

class DisplayedTimelineEvent(Event):
  name: str = "displayed_timeline"
  label: str = "Displayed Timeline Event"

  def __init__(self, data: Dict[str, Any]):
    super().__init__(data)
