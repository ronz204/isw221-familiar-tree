from typing import Dict, List
from Application.Events.Event import Event
from Application.Events.Listener import Listener

class Broker:
  def __init__(self):
    self.listeners: Dict[str, List[Listener]] = {}

  def subscribe(self, event: str, listener: Listener) -> None:
    if event not in self.listeners:
      self.listeners[event] = []

    if listener not in self.listeners[event]:
      self.listeners[event].append(listener)

  def unsubscribe(self, event: str, listener: Listener) -> None:
    if event in self.listeners and listener in self.listeners[event]:
      self.listeners[event].remove(listener)

  def publish(self, event: Event) -> None:
    if event.name not in self.listeners: return

    for listener in self.listeners[event.name]:
      try:
        listener.listen(event)
      except Exception as err:
        print(f"Error occurred while handling event '{event.name}': {err}")
