from Events.Event import Event

class BirthdaysPersonEvent(Event):
  name = "birthdays_person"

  def __init__(self, data = None):
    super().__init__(data)
