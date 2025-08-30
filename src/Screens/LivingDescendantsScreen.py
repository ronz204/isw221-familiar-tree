import tkinter as tk
from typing import Dict, Any, List
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener

from Builders.LivingDescendantsScreenBuilder import LivingDescendantsScreenBuilder
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent
from Handlers.Queries.LivingDescendants.LivingDescendantsEvent import LivingDescendantsEvent
from Handlers.Queries.LivingDescendants.LivingDescendantsHandler import LivingDescendantsHandler

class LivingDescendantsScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = LivingDescendantsScreenBuilder(self)
    self.living_descendants_handler = LivingDescendantsHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_person_field()
    self.builder.build_result_list()

    self.builder.build_search_button(self.on_search_descendants)
    self.builder.build_clear_button(self.on_clear_form)
    self.builder.load_data_hydration()

  def subscribe_to_events(self):
    self.broker.subscribe(LivingDescendantsEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_living_descendants_result(self, data: Dict[str, Any]):
    descendants: List[Dict[str, Any]] = data.get("living_descendants", [])
    person_id = data.get("person_id")

    person_name = "Persona desconocida"
    if person_id:
      selected_index = self.builder.person_combo.current()
      if selected_index > 0:
        person_name = self.builder.people[selected_index - 1].name
    
    self.builder.set_descendants_result(descendants, person_name)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()

  def handle(self, event: Event):
    if event.name == LivingDescendantsEvent.name:
      self.on_living_descendants_result(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_search_descendants(self):
    data = self.builder.get_form_data()
    self.living_descendants_handler.execute(data)

  def on_clear_form(self):
    self.builder.clear_form()
