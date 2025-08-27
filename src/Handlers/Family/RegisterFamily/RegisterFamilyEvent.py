from Events.Event import Event

class RegisterFamilyEvent(Event):
  def __init__(self, data = None):
    super().__init__("register_family", data)
