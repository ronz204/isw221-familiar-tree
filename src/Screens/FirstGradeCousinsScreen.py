import tkinter as tk
from Events.Event import Event
from Events.Broker import Broker
from Models.Person import Person
from typing import Dict, Any, List
from Events.Listener import Listener

from Builders.FirstGradeCousinsScreenBuilder import FirstGradeCousinsScreenBuilder
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent
from Handlers.Queries.FirstGradeCousins.FirstGradeCousinsEvent import FirstGradeCousinsEvent
from Handlers.Queries.FirstGradeCousins.FirstGradeCousinsHandler import FirstGradeCousinsHandler

class FirstGradeCousinsScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = FirstGradeCousinsScreenBuilder(self)
    self.first_grade_cousins_handler = FirstGradeCousinsHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_person_field()
    self.builder.build_result_list()

    self.builder.build_search_button(self.on_search_cousins)
    self.builder.build_clear_button(self.on_clear_form)
    self.builder.load_data_hydration()

  def subscribe_to_events(self):
    self.broker.subscribe(FirstGradeCousinsEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_first_grade_cousins_result(self, data: Dict[str, Any]):
    cousins: List[Person] = data.get("cousins", [])
    person_name: str = data.get("person_name", "")
    
    self.builder.set_cousins_result(cousins, person_name)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()

  def handle(self, event: Event):
    if event.name == FirstGradeCousinsEvent.name:
      self.on_first_grade_cousins_result(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_search_cousins(self):
    data = self.builder.get_form_data()
    self.first_grade_cousins_handler.execute(data)

  def on_clear_form(self):
    self.builder.clear_form()