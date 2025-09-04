import tkinter as tk
from Application.Events.Broker import Broker
from Presentation.Screens.Person.PersonBuilder import PersonBuilder
from Application.Handlers.RegisterPerson.RegisterPersonHandler import RegisterPersonHandler

class PersonScreen(tk.Frame):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker

    self.builder = PersonBuilder(self)
    self.register_person_handler = RegisterPersonHandler(broker)

    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_container()
    self.builder.build_frames()
    self.builder.build_title()

    self.builder.load_data_hydration()

    self.builder.build_age_field()
    self.builder.build_name_field()
    self.builder.build_cedula_field()
    self.builder.build_birthdate_field()
    self.builder.build_deathdate_field()
    self.builder.build_emotional_field()
    self.builder.build_gender_field()
    self.builder.build_province_field()
    self.builder.build_affinity_checks()

    self.builder.build_register_button(self.register_command)
    self.builder.build_discard_button(self.discard_command)

  def register_command(self):
    data = self.builder.get_form_data()
    self.register_person_handler.handle(data)
    self.builder.clear_form_fields()

  def discard_command(self):
    self.builder.clear_form_fields()
