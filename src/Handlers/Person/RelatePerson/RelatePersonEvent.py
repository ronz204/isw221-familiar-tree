from Events.Event import Event

class RelatePersonEvent(Event):
  name = "relate_person"
  label = "Relate Person"

  def __init__(self, data = None):
    super().__init__(data)
