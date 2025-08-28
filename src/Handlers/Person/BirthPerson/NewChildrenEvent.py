from Events.Event import Event

class NewChildrenEvent(Event):
  name = "new_children"
  label = "New Children"

  def __init__(self, data = None):
    super().__init__(data)
