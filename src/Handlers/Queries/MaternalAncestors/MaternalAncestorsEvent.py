from Events.Event import Event

class MaternalAncestorsEvent(Event):
  name = "maternal_ancestors"
  label = "Maternal Ancestors"

  def __init__(self, data = None):
    super().__init__(data)
