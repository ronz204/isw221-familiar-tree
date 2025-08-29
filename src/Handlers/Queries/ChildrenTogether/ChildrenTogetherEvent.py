from Events.Event import Event

class ChildrenTogetherEvent(Event):
  name = "children_together"
  label = "Children Together"

  def __init__(self, data = None):
    super().__init__(data)
