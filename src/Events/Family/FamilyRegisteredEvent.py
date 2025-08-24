from Events.Event import Event

class FamilyRegisteredEvent(Event):
  def __init__(self, data = None):
    super().__init__("family_registered", data)
