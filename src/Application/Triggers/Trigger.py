from abc import ABC, abstractmethod
from Application.Events.Broker import Broker

class Trigger(ABC):
  def __init__(self, broker: Broker):
    self.broker: Broker = broker

  @abstractmethod
  def trigger(self) -> None:
    pass
