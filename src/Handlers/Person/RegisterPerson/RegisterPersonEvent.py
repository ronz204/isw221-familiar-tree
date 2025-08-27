from Events.Event import Event

class RegisterPersonEvent(Event):
  def __init__(self, data = None):
    super().__init__("register_person", data)
