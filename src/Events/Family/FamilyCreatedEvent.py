from Events.Event import Event

class FamilyCreatedEvent(Event):
  def __init__(self, data = None):
    super().__init__("family_created", data)
