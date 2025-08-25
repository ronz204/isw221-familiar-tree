import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener
from Builders.PersonScreenBuilder import PersonScreenBuilder
from Handlers.Person.RegisterPerson.RegisterPersonHandler import RegisterPersonHandler

class PersonScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = PersonScreenBuilder(self)
    self.register_person_handler = RegisterPersonHandler(broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_name_field()
    self.builder.build_cedula_field()
    self.builder.build_province_field()
    self.builder.build_age_field()
    self.builder.build_birthdate_field()
    self.builder.build_emotional_field()

    self.builder.build_gender_field()
    self.builder.build_family_field()
    self.builder.build_father_field()
    self.builder.build_mother_field()

    self.builder.build_save_button(self.on_save_person)
    self.builder.build_discard_button(self.on_discard_person)
    self.builder.load_data_hydration()

  def subscribe_to_events(self):
    self.broker.subscribe("person_registered", self)

  def on_person_registered(self, data: Dict[str, Any]):
    print("Person registered with data:", data)
    self.builder.load_data_hydration()

  def handle(self, event: Event):
    if event.name == "person_registered":
      self.on_person_registered(event.data)

  def on_save_person(self):
    data = self.builder.get_form_data()
    self.register_person_handler.execute(data)
    self.builder.clear_form()

  def on_discard_person(self):
    self.builder.clear_form()
