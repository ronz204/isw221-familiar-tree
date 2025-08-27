from Events.Event import Event

class RelateCoupleEvent(Event):
  name = "relate_couple"
  
  def __init__(self, data = None):
    super().__init__(data)
