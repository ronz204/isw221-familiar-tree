from Events.Event import Event

class BirthdaysPersonEvent(Event):
  def __init__(self, data = None):
    super().__init__("birthdays_person", data)
