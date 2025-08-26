from Events.Event import Event

class BirthdateEvent(Event):
  def __init__(self, data = None):
    super().__init__("birthdate", data)
