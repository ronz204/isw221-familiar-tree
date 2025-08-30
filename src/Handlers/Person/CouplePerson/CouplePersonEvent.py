from Events.Event import Event

class CouplePersonEvent(Event):
  name = "couple_person"
  label = "Couple Person"

  def __init__(self, data = None):
    super().__init__(data)
