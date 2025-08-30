from Events.Event import Event

class RelatePeopleEvent(Event):
  name = "relate_people"
  label = "Relate People"

  def __init__(self, data = None):
    super().__init__(data)
