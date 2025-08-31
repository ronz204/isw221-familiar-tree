from typing import Dict, Any

class Event:
  name: str = None
  label: str = None

  def __init__(self, data: Dict[str, Any] = {}):
    self.data: Dict[str, Any] = data
