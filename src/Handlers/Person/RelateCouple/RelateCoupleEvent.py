from Events.Event import Event

class RelateCoupleEvent(Event):
  def __init__(self, data = None):
    super().__init__("relate_couple", data)
