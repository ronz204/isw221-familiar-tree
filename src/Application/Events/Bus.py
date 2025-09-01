from typing import Dict, Callable

class Bus:
  def __init__(self):
    self.map: Dict[str, Callable] = {}

  def add(self, key: str, func: Callable):
    self.map[key] = func

  def get(self, key: str) -> Callable | None:
    return self.map.get(key)
