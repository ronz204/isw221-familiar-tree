import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Domain.Models.Person import Person
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Family.FamilyBuilder import FamilyBuilder

class FamilyScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = FamilyBuilder(self)

    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_title()
    self.builder.build_canvas()
    self.builder.build_scrollers()

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  """ def load_and_draw_tree(self):
    people = list(Person.select())
    self.builder.draw_tree(people) """