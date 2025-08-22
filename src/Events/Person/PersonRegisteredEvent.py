from Events.Event import Event

class PersonRegisteredEvent(Event):
  def __init__(self, data = None):
    super().__init__("person_registered", data)
