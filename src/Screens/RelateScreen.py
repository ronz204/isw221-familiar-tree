import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener
from Builders.RelateScreenBuilder import RelateScreenBuilder
from Handlers.Person.RelateCouple.RelateCoupleHandler import RelateCoupleHandler

class RelateScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = RelateScreenBuilder(self)
    self.relate_couple_handler = RelateCoupleHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_person1_field()
    self.builder.build_person2_field()

    self.builder.build_relate_button(self.on_relate_couple)
    self.builder.build_discard_button(self.on_discard_relation)
    self.builder.load_data_hydration()

  def subscribe_to_events(self):
    self.broker.subscribe("couple_related", self)
    self.broker.subscribe("person_registered", self)
  
  def on_couple_related(self, data: Dict[str, Any]):
    print(f"Couple related: {data["person1_name"]} and {data["person2_name"]}")
    self.builder.load_data_hydration()
    self.builder.clear_form()

  def on_person_registered(self, data: Dict[str, Any]):
    print(f"Person registered: {data["name"]}")
    self.builder.load_data_hydration()

  def handle(self, event: Event):
    if event.name == "couple_related":
      self.on_couple_related(event.data)
    elif event.name == "person_registered":
      self.on_person_registered(event.data)
  
  def on_relate_couple(self):
    data = self.builder.get_form_data()
    if not data["person1_id"] or not data["person2_id"]: return
    self.relate_couple_handler.execute(data)

  def on_discard_relation(self):
    self.builder.clear_form()
