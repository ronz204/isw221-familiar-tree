from Events.Event import Event

class RegisterFamilyEvent(Event):
  name = "register_family"

  def __init__(self, data = None):
    super().__init__(data)
