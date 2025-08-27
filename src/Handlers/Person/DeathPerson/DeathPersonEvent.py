from Events.Event import Event

class DeathPersonEvent(Event):
  name = "death_person"
  
  def __init__(self, data = None):
    super().__init__(data)
