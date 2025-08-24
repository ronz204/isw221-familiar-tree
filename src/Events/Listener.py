from Events.Event import Event

class Listener:
  def handle(self, event: Event) -> None:
    raise NotImplementedError("This method should be overridden by subclasses")
