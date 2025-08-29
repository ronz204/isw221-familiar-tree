import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener

from Builders.BetweenPeopleScreenBuilder import BetweenPeopleScreenBuilder
from Handlers.Queries.BetweenPeople.BetweenPeopleHandler import BetweenPeopleHandler
from Handlers.Queries.BetweenPeople.BetweenPeopleEvent import BetweenPeopleEvent
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent

class BetweenPeopleScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = BetweenPeopleScreenBuilder(self)
    self.between_people_handler = BetweenPeopleHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_person1_field()
    self.builder.build_person2_field()
    self.builder.build_result_label()

    self.builder.build_find_button(self.on_find_relationship)
    self.builder.build_clear_button(self.on_clear_form)
    self.builder.load_data_hydration()

  def subscribe_to_events(self):
    self.broker.subscribe(BetweenPeopleEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_between_people_result(self, data: Dict[str, Any]):
    relationship = data.get("relationship", "")
    self.builder.set_result(relationship)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()

  def handle(self, event: Event):
    if event.name == BetweenPeopleEvent.name:
      self.on_between_people_result(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_find_relationship(self):
    data = self.builder.get_form_data()
    
    # Validar que ambas personas estén seleccionadas
    if not data["person1_id"] or not data["person2_id"]:
      self.builder.set_result("")
      return
    
    # Validar que no sean la misma persona
    if data["person1_id"] == data["person2_id"]:
      self.builder.result_label.config(text="No puedes seleccionar la misma persona dos veces", fg="red")
      return
    
    # Ejecutar el handler
    self.between_people_handler.execute({
      "person1": data["person1_id"],
      "person2": data["person2_id"]
    })

  def on_clear_form(self):
    self.builder.clear_form()
