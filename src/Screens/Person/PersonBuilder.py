import tkinter as tk
from Components.Field import Field
from Components.Combo import Combo
from Components.Button import Button
from typing import Any, Callable, Dict

GENDER_OPTIONS = ["M", "F"]

PROVINCE_OPTIONS = [
  "Alajuela", "San José",
  "Puntarenas", "Guanacaste",
  "Heredia", "Cartago", "Limon",
]

class PersonBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent: tk.Widget = parent

  def build_grid_config(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)

  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid_columnconfigure(1, weight=1)
    self.container.grid_columnconfigure(2, weight=1)
    self.container.grid(row=1, column=1, padx=30, pady=30)

  def build_frames(self):
    self.form_frame = tk.Frame(self.container)
    self.form_frame.grid(row=1, column=0, columnspan=3, sticky=tk.EW, pady=(0, 20))
    self.form_frame.grid_columnconfigure(0, weight=1)
    self.form_frame.grid_columnconfigure(1, weight=1)
    
    self.buttons_frame = tk.Frame(self.container)
    self.buttons_frame.grid(row=2, column=0, columnspan=3, sticky=tk.EW)
    self.buttons_frame.grid_columnconfigure(0, weight=1)

  def build_title(self):
    self.title = tk.Label(self.container, text="Registrar una Nueva Persona", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=3, pady=(0, 25))

  def build_name_field(self):
    self.name_field = Field(self.form_frame, "Nombre")
    self.name_field.label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
    self.name_field.entry.grid(row=1, column=1, sticky=tk.EW, pady=(0, 12))

  def build_cedula_field(self):
    self.cedula_field = Field(self.form_frame, "Cédula")
    self.cedula_field.label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
    self.cedula_field.entry.grid(row=2, column=1, sticky=tk.EW, pady=(0, 12))

  def build_age_field(self):
    self.age_field = Field(self.form_frame, "Edad")
    self.age_field.label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
    self.age_field.entry.grid(row=3, column=1, sticky=tk.EW, pady=(0, 12))

  def build_birthdate_field(self):
    self.birthdate_field = Field(self.form_frame, "Fecha de Nacimiento")
    self.birthdate_field.label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
    self.birthdate_field.entry.grid(row=4, column=1, sticky=tk.EW, pady=(0, 12))

  def build_deathdate_field(self):
    self.deathdate_field = Field(self.form_frame, "Fecha de Fallecimiento")
    self.deathdate_field.label.grid(row=5, column=0, sticky=tk.W, pady=(0, 5))
    self.deathdate_field.entry.grid(row=5, column=1, sticky=tk.EW, pady=(0, 12))

  def build_emotional_field(self):
    self.emotional_field = Field(self.form_frame, "Estado Emocional")
    self.emotional_field.label.grid(row=6, column=0, sticky=tk.W, pady=(0, 5))
    self.emotional_field.entry.grid(row=6, column=1, sticky=tk.EW, pady=(0, 12))
    self.emotional_field.entry.insert(0, "100")

  def build_gender_field(self):
    self.gender_combo = Combo(self.form_frame, "Género", GENDER_OPTIONS)
    self.gender_combo.label.grid(row=7, column=0, sticky=tk.W, pady=(0, 5))
    self.gender_combo.combobox.grid(row=7, column=1, sticky=tk.EW, pady=(0, 12))

  def build_province_field(self):
    self.province_combo = Combo(self.form_frame, "Provincia", PROVINCE_OPTIONS)
    self.province_combo.label.grid(row=8, column=0, sticky=tk.W, pady=(0, 5))
    self.province_combo.combobox.grid(row=8, column=1, sticky=tk.EW, pady=(0, 12))

  def build_register_button(self, command: Callable):
    self.register_button = Button(self.buttons_frame, "Registrar", command=command)
    self.register_button.grid(row=0, column=0, pady=(10, 0))

  def build_discard_button(self, command: Callable):
    self.discard_button = Button(self.buttons_frame, "Descartar", command=command)
    self.discard_button.grid(row=0, column=1, pady=(10, 0))

  def get_form_data(self) -> Dict[str, Any]:
    return {
      "name": self.name_field.entry.get(),
      "cedula": self.cedula_field.entry.get(),
      "age": int(self.age_field.entry.get() or 0),
      "birthdate": self.birthdate_field.entry.get(),
      "deathdate": self.deathdate_field.entry.get() or None,
      "emotional": int(self.emotional_field.entry.get() or 100),
      "gender": self.gender_combo.combobox.get(),
      "province": self.province_combo.combobox.get(),
    }
  
  def clear_form_fields(self):
    self.age_field.entry.delete(0, tk.END)
    self.name_field.entry.delete(0, tk.END)
    self.cedula_field.entry.delete(0, tk.END)
    self.birthdate_field.entry.delete(0, tk.END)
    self.deathdate_field.entry.delete(0, tk.END)
    self.emotional_field.entry.delete(0, tk.END)
    self.emotional_field.entry.insert(0, "100")
    self.gender_combo.combobox.set("")
    self.province_combo.combobox.set("")
