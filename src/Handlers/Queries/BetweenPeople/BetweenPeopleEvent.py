from Events.Event import Event

class BetweenPeopleEvent(Event):
  name = "between_people"
  label = "Between People"

  def __init__(self, data = None):
    super().__init__(data)
