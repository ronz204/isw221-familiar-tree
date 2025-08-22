from typing import Dict, List
from Events.Event import Event
from Handlers.Handler import Handler

class EventBroker:
  def __init__(self):
    self.listeners: Dict[str, List[Handler]] = {}

  def subscribe(self, event: str, listener: Handler) -> None:
    if event not in self.listeners:
      self.listeners[event] = []

    if listener not in self.listeners[event]:
      self.listeners[event].append(listener)

  def unsubscribe(self, event: str, listener: Handler) -> None:
    if event in self.listeners and listener in self.listeners[event]:
      self.listeners[event].remove(listener)

  def publish(self, event: Event) -> None:
    if event.name in self.listeners:
      for listener in self.listeners[event.name]:

        try:
          listener.handle(event)
        except Exception as err:
          print(f"Error occurred while handling event '{event.name}': {err}")
