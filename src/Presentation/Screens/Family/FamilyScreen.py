import tkinter as tk
from Application.Events.Bus import Bus
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

    self.builder.build_legend_info()
    self.setup_family_tree()

  def setup_family_tree(self):
    self.builder.load_data_hydration()
    self.builder.build_family_tree()

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)
