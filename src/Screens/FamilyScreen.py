import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener
from Builders.FamilyScreenBuilder import FamilyScreenBuilder
from Handlers.Family.RegisterFamily.RegisterFamilyHandler import RegisterFamilyHandler

class FamilyScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = FamilyScreenBuilder(self)
    self.register_family_handler = RegisterFamilyHandler(broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_frames()

    self.builder.build_title()
    self.builder.build_name_field()
    
    self.builder.build_save_button(self.on_save_family)
    self.builder.build_discard_button(self.on_discard_family)

  def subscribe_to_events(self):
    self.broker.subscribe("family_created", self)

  def on_family_created(self, data: Dict[str, Any]):
    print("Family created with data:", data)

  def handle(self, event: Event):
    if (event.name == "family_created"):
      self.on_family_created(event.data)

  def on_save_family(self):
    family_name = self.builder.name_entry.get()
    self.register_family_handler.execute(family_name)
    self.builder.name_entry.delete(0, tk.END)

  def on_discard_family(self):
    self.builder.name_entry.delete(0, tk.END)
