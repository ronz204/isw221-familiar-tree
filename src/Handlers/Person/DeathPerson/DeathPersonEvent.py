from Events.Event import Event

class DeathPersonEvent(Event):
  def __init__(self, data = None):
    super().__init__("death_person", data)
