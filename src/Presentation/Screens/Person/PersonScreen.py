import tkinter as tk

from Presentation.Screens.Person.PersonBuilder import PersonBuilder

class PersonScreen(tk.Frame):
  def __init__(self, parent: tk.Widget):
    super().__init__(parent)

    self.builder = PersonBuilder(self)

    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_grid_config()
    self.builder.build_container()
    self.builder.build_frames()
    self.builder.build_title()

    self.builder.build_age_field()
    self.builder.build_name_field()
    self.builder.build_cedula_field()
    self.builder.build_birthdate_field()
    self.builder.build_deathdate_field()
    self.builder.build_emotional_field()
    self.builder.build_gender_field()
    self.builder.build_province_field()

    self.builder.build_register_button(self.register_command)
    self.builder.build_discard_button(self.discard_command)

  def register_command(self):
    data = self.builder.get_form_data()
    print(data)

  def discard_command(self):
    self.builder.clear_form_fields()
