from abc import ABC, abstractmethod
from Application.Events.Event import Event

class Listener(ABC):
  @abstractmethod
  def listen(self, event: Event) -> None: pass
