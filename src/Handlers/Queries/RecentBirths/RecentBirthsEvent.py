from Events.Event import Event

class RecentBirthsEvent(Event):
  name = "recent_births"
  label = "Recent Births"

  def __init__(self, data = None):
    super().__init__(data)
