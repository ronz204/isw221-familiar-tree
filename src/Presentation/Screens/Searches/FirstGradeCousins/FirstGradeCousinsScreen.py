import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Searches.FirstGradeCousins.FirstGradeCousinsBuilder import FirstGradeCousinsBuilder
from Application.Handlers.Searchers.FirstGradeCousins.FirstGradeCousinsHandler import FirstGradeCousinsHandler

from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.CousinsFoundEvent import CousinsFoundEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class FirstGradeCousinsScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = FirstGradeCousinsBuilder(self)
    self.first_grade_cousins_handler = FirstGradeCousinsHandler(self.broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(PersonBornEvent.name, self)
    self.broker.subscribe(CousinsFoundEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)

    self.bus.add(PersonBornEvent.name, self.on_person_born)
    self.bus.add(CousinsFoundEvent.name, self.on_cousins_found)
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
    
    self.first_grade_cousins_handler.handle({
      "person_id": data["person_id"]
    })

  def on_clear_command(self):
    self.builder.clear_form_fields()

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_cousins_found(self, data: Dict[str, Any]):
    cousins = data.get("cousins", [])
    person_id = data.get("person_id")
    
    selected_person_name = "la persona seleccionada"
    if person_id:
      for person in self.builder.persons:
        if person.id == person_id:
          selected_person_name = person.name
          break
    
    self.builder.display_results(cousins, selected_person_name)

  def on_registered_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
    self.builder.clear_results()

  def on_person_born(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
