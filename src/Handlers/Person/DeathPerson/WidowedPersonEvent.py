from Events.Event import Event

class WidowedPersonEvent(Event):
  name = "widowed_person"
  label = "Widowed Person"

  def __init__(self, data = None):
    super().__init__(data)
