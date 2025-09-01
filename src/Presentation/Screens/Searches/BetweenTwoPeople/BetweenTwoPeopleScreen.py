import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Searches.BetweenTwoPeople.BetweenTwoPeopleBuilder import BetweenTwoPeopleBuilder
from Application.Handlers.Searchers.BetweenTwoPeople.BetweenTwoPeopleHandler import BetweenTwoPeopleHandler

from Application.Events.Person.RelativesFoundEvent import RelativesFoundEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class BetweenTwoPeopleScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = BetweenTwoPeopleBuilder(self)
    self.between_people_handler = BetweenTwoPeopleHandler(self.broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(RelativesFoundEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)

    self.bus.add(RelativesFoundEvent.name, self.on_relatives_found_result)
    self.bus.add(RegisteredPersonEvent.name, self.on_register_person)

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()
    
    self.builder.build_person1_field()
    self.builder.build_person2_field()
    self.builder.build_result_section()
    
    self.builder.build_find_button(self.on_find_relationship)
    self.builder.build_clear_button(self.on_clear_form)
    
    self.builder.load_data_hydration()

  def on_find_relationship(self):
    data = self.builder.get_form_data()
    
    if not data["person1_id"] or not data["person2_id"]:
      self.builder.set_result("")
      return
    
    if data["person1_id"] == data["person2_id"]:
      self.builder.result_label.config(text="No puedes seleccionar la misma persona dos veces", fg="red")
      return

    self.between_people_handler.handle({
      "person1_id": data["person1_id"],
      "person2_id": data["person2_id"]
    })

  def on_clear_form(self):
    self.builder.clear_form_fields()

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_relatives_found_result(self, data: Dict[str, Any]):
    relationship = data.get("relation", "")
    self.builder.set_result(relationship)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
