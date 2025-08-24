from Events.Broker import Broker

class Handler:
  def __init__(self, broker: Broker):
    self.broker: Broker = broker

  def execute(self) -> None:
    raise NotImplementedError("This method should be overridden by subclasses")
