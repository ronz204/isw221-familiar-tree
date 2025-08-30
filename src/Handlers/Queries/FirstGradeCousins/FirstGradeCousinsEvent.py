from Events.Event import Event

class FirstGradeCousinsEvent(Event):
  name = "first_grade_cousins"
  label = "First Grade Cousins"

  def __init__(self, data = None):
    super().__init__(data)
