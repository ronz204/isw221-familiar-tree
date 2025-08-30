from Events.Event import Event

class LivingDescendantsEvent(Event):
  name = "living_descendants"
  label = "Living Descendants"

  def __init__(self, data = None):
    super().__init__(data)
