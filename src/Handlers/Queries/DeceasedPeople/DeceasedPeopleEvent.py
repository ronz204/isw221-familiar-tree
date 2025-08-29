from Events.Event import Event

class DeceasedPeopleEvent(Event):
  name = "deceased_people"
  label = "Deceased People"

  def __init__(self, data = None):
    super().__init__(data)
