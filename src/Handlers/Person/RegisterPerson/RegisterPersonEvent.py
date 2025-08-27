from Events.Event import Event

class RegisterPersonEvent(Event):
  name = "register_person"
  
  def __init__(self, data = None):
    super().__init__(data)
