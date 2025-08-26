from Events.Event import Event

class DeathdateEvent(Event):
  def __init__(self, data = None):
    super().__init__("deathdate", data)
