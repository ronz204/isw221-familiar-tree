from typing import Any

class Event:
  name: str = None
  label: str = None

  def __init__(self, data: Any = None):
    self.data = data
