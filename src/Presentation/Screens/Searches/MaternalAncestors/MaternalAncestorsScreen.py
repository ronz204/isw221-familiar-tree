import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Searches.MaternalAncestors.MaternalAncestorsBuilder import MaternalAncestorsBuilder
from Application.Handlers.Searchers.MaternalAncestors.MaternalAncestorsHandler import MaternalAncestorsHandler

from Application.Events.Person.MaternalAncestorsFoundEvent import MaternalAncestorsFoundEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class MaternalAncestorsScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = MaternalAncestorsBuilder(self)
    self.maternal_ancestors_handler = MaternalAncestorsHandler(self.broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(MaternalAncestorsFoundEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)

    self.bus.add(MaternalAncestorsFoundEvent.name, self.on_ancestors_found)
    self.bus.add(RegisteredPersonEvent.name, self.on_registered_person)

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()
    self.builder.build_person_field()

    self.builder.build_search_button(self.on_search_command)
    self.builder.build_clear_button(self.on_clear_command)

    self.builder.build_result_section()
    self.builder.build_info_label()
    self.builder.load_data_hydration()
    self.builder.clear_results()

  def on_search_command(self):
    data = self.builder.get_form_data()
    
    if not data["person_id"]:
      self.builder.clear_results()
      self.builder.info_label.config(text="Por favor selecciona una persona", fg="red")
      return
    
    self.maternal_ancestors_handler.handle({
      "person_id": data["person_id"]
    })

  def on_clear_command(self):
    self.builder.clear_form_fields()

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_ancestors_found(self, data: Dict[str, Any]):
    ancestors = data.get("ancestors", [])
    person_id = data.get("person_id")
    
    selected_person_name = "la persona seleccionada"
    if person_id:
      for person in self.builder.persons:
        if person.id == person_id:
          selected_person_name = person.name
          break
    
    self.builder.display_results(ancestors, selected_person_name)

  def on_registered_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
    self.builder.clear_results()
