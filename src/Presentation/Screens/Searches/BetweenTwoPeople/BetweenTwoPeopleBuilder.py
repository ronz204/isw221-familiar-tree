import tkinter as tk
from Domain.Models.Person import Person
from typing import Any, Callable, Dict, List
from Presentation.Components.Combo import Combo
from Presentation.Components.Button import Button

class BetweenTwoPeopleBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent: tk.Widget = parent

  def setup_grid(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)

  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid(row=1, column=1, padx=40, pady=40, sticky=tk.NSEW)

  def build_title(self):
    self.title = tk.Label(self.container, text="Encontrar Parentesco", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=2, pady=(0, 25))

  def build_frames(self):
    self.form_frame = tk.Frame(self.container)
    self.form_frame.grid_columnconfigure(0, weight=1)
    self.form_frame.grid_columnconfigure(1, weight=1)
    self.form_frame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, pady=(0, 20))

    self.result_frame = tk.Frame(self.container)
    self.result_frame.grid_columnconfigure(0, weight=1)
    self.result_frame.grid(row=2, column=0, columnspan=2, sticky=tk.EW, pady=(0, 20))

    self.button_frame = tk.Frame(self.container)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(1, weight=1)
    self.button_frame.grid(row=3, column=0, columnspan=2, sticky=tk.EW)

  def build_person1_field(self):
    self.person1_combo = Combo(self.form_frame, "Primera Persona", [])
    self.person1_combo.label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5), padx=(0, 10))
    self.person1_combo.combobox.grid(row=1, column=0, sticky=tk.EW, pady=(0, 15), padx=(0, 10))

  def build_person2_field(self):
    self.person2_combo = Combo(self.form_frame, "Segunda Persona", [])
    self.person2_combo.label.grid(row=0, column=1, sticky=tk.W, pady=(0, 5), padx=(10, 0))
    self.person2_combo.combobox.grid(row=1, column=1, sticky=tk.EW, pady=(0, 15), padx=(10, 0))

  def build_result_section(self):
    self.result_title = tk.Label(self.result_frame, text="Parentesco:", font=("", 12, "bold"))
    self.result_title.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
    
    self.result_label = tk.Label(self.result_frame, text="Selecciona dos personas y presiona 'Buscar Parentesco'", 
                                font=("", 11), fg="gray", wraplength=400, justify="left")
    self.result_label.grid(row=1, column=0, sticky=tk.W)

  def build_find_button(self, command: Callable):
    self.find_button = Button(self.button_frame, "Buscar Parentesco", command)
    self.find_button.config(width=20, height=2, font=("", 11, "bold"))
    self.find_button.grid(row=0, column=0, padx=(0, 10), sticky=tk.E)

  def build_clear_button(self, command: Callable):
    self.clear_button = Button(self.button_frame, "Limpiar", command)
    self.clear_button.config(width=15, height=2, font=("", 11, "bold"))
    self.clear_button.grid(row=0, column=1, padx=(10, 0), sticky=tk.W)

  def load_data_hydration(self):
    self.persons: List[Person] = list(Person.select())
    person_names = [""] + [person.name for person in self.persons]
    
    self.person1_combo.combobox["values"] = person_names
    self.person2_combo.combobox["values"] = person_names

  def get_selected_id(self, combo_value: str, records: List[Person]):
    for person in records:
      if person.name == combo_value:
        return person.id
    return None

  def get_form_data(self) -> Dict[str, Any]:
    return {
      "person1_id": self.get_selected_id(self.person1_combo.combobox.get(), self.persons),
      "person2_id": self.get_selected_id(self.person2_combo.combobox.get(), self.persons)
    }

  def clear_form_fields(self):
    self.person1_combo.combobox.set("")
    self.person2_combo.combobox.set("")
    self.result_label.config(text="Selecciona dos personas y presiona 'Buscar Parentesco'", fg="gray")

  def set_result(self, relationship: str):
    if relationship:
      self.result_label.config(text=relationship, fg="black")
    else:
      self.result_label.config(text="No se encontró parentesco entre estas personas", fg="red")
