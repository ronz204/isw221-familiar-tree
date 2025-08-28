from Events.Event import Event

class BirthPersonEvent(Event):
  name = "birth_person"
  label = "Birth Person"

  def __init__(self, data = None):
    super().__init__(data)
