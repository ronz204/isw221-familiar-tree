import tkinter as tk
from Domain.Models.Person import Person
from typing import Any, Callable, Dict, List
from Presentation.Components.Combo import Combo
from Presentation.Components.Button import Button

class RelateBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent: tk.Widget = parent

  def setup_grid(self):
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
    self.title = tk.Label(self.container, text="Relacionar Personas", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=3, pady=(0, 25))

  def build_person_field(self):
    self.person_combo = Combo(self.form_frame, "Persona", [])
    self.person_combo.label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
    self.person_combo.combobox.grid(row=1, column=1, sticky=tk.EW, pady=(0, 12))

  def build_father_field(self):
    self.father_combo = Combo(self.form_frame, "Padre", [])
    self.father_combo.label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
    self.father_combo.combobox.grid(row=2, column=1, sticky=tk.EW, pady=(0, 12))

  def build_mother_field(self):
    self.mother_combo = Combo(self.form_frame, "Madre", [])
    self.mother_combo.label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
    self.mother_combo.combobox.grid(row=3, column=1, sticky=tk.EW, pady=(0, 12))

  def build_guardian_field(self):
    self.guardian_combo = Combo(self.form_frame, "Guardian", [])
    self.guardian_combo.label.grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
    self.guardian_combo.combobox.grid(row=4, column=1, sticky=tk.EW, pady=(0, 12))

  def build_relate_button(self, command: Callable):
    self.relate_button = Button(self.buttons_frame, "Relacionar", command=command)
    self.relate_button.grid(row=0, column=0, pady=(10, 0))

  def build_clear_button(self, command: Callable):
    self.clear_button = Button(self.buttons_frame, "Limpiar", command=command)
    self.clear_button.grid(row=0, column=1, pady=(10, 0))

  def load_data_hydration(self):
    self.persons: List[Person] = list(Person.select())
    person_names = [""] + [person.name for person in self.persons]
    self.person_combo.combobox["values"] = person_names

    self.fathers: List[Person] = list(Person.select().where(Person.gender == "M"))
    father_names = [""] + [father.name for father in self.fathers]
    self.father_combo.combobox["values"] = father_names

    self.mothers: List[Person] = list(Person.select().where(Person.gender == "F"))
    mother_names = [""] + [mother.name for mother in self.mothers]
    self.mother_combo.combobox["values"] = mother_names

    self.guardians: List[Person] = list(Person.select())
    guardian_names = [""] + [guardian.name for guardian in self.guardians]
    self.guardian_combo.combobox["values"] = guardian_names

  def get_selected_id(self, combo_value: str, records: List[Person]):
    for person in records:
      if person.name == combo_value:
        return person.id
    return None

  def get_form_data(self) -> Dict[str, Any]:
    return {
      "person_id": self.get_selected_id(self.person_combo.combobox.get(), self.persons),
      "father_id": self.get_selected_id(self.father_combo.combobox.get(), self.fathers),
      "mother_id": self.get_selected_id(self.mother_combo.combobox.get(), self.mothers),
      "guard_id": self.get_selected_id(self.guardian_combo.combobox.get(), self.guardians),
    }

  def clear_form_fields(self):
    self.person_combo.combobox.set("")
    self.father_combo.combobox.set("")
    self.mother_combo.combobox.set("")
    self.guardian_combo.combobox.set("")
