from Events.Event import Event

class CoupleRelatedEvent(Event):
  def __init__(self, data = None):
    super().__init__("couple_related", data)
