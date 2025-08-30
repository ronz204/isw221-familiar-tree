import tkinter as tk
from tkinter import ttk
from Models.Person import Person
from typing import Any, Callable, List

class RelatePeopleScreenBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent = parent

  def build_layout(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)

  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid_columnconfigure(1, weight=1)
    self.container.grid(row=1, column=1, padx=30, pady=30)

  def build_title(self):
    self.title = tk.Label(self.container, text="Relacionar Personas", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=2, pady=(0, 25))

  def build_frames(self):
    self.left_frame = tk.Frame(self.container)
    self.left_frame.grid_columnconfigure(0, weight=1)
    self.left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 15))
    
    self.right_frame = tk.Frame(self.container)
    self.right_frame.grid_columnconfigure(0, weight=1)
    self.right_frame.grid(row=1, column=1, sticky="nsew", padx=(15, 0))

  def build_person_field(self):
    self.person_label = tk.Label(self.left_frame, text="Persona:")
    self.person_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
    self.person_combo = ttk.Combobox(self.left_frame, state="readonly", width=25)
    self.person_combo.grid(row=2, column=0, sticky="ew", pady=(0, 12))

  def build_father_field(self):
    self.father_label = tk.Label(self.left_frame, text="Padre:")
    self.father_label.grid(row=3, column=0, sticky="w", pady=(0, 5))
    self.father_combo = ttk.Combobox(self.left_frame, state="readonly", width=25)
    self.father_combo.grid(row=4, column=0, sticky="ew", pady=(0, 12))

  def build_mother_field(self):
    self.mother_label = tk.Label(self.left_frame, text="Madre:")
    self.mother_label.grid(row=5, column=0, sticky="w", pady=(0, 5))
    self.mother_combo = ttk.Combobox(self.left_frame, state="readonly", width=25)
    self.mother_combo.grid(row=6, column=0, sticky="ew", pady=(0, 12))

  def build_guardian_field(self):
    self.guardian_label = tk.Label(self.left_frame, text="Guardian:")
    self.guardian_label.grid(row=7, column=0, sticky="w", pady=(0, 5))
    self.guardian_combo = ttk.Combobox(self.left_frame, state="readonly", width=25)
    self.guardian_combo.grid(row=8, column=0, sticky="ew", pady=(0, 12))

  def build_relate_button(self, command: Callable):
    self.relate_button = tk.Button(self.right_frame, text="Relacionar", command=command)
    self.relate_button.config(width=12, height=2, font=("", 11, "bold"))
    self.relate_button.grid(row=1, column=0, pady=(0, 15))

  def build_clear_button(self, command: Callable):
    self.clear_button = tk.Button(self.right_frame, text="Limpiar", command=command)
    self.clear_button.config(width=12, height=2, font=("", 11, "bold"))
    self.clear_button.grid(row=2, column=0)

  def load_data_hydration(self):
    self.persons: List[Person] = list(Person.select())
    self.person_combo["values"] = [""] + [person.name for person in self.persons]

    self.fathers: List[Person] = list(Person.select().where(Person.gender == "M"))
    self.father_combo["values"] = [""] + [father.name for father in self.fathers]

    self.mothers: List[Person] = list(Person.select().where(Person.gender == "F"))
    self.mother_combo["values"] = [""] + [mother.name for mother in self.mothers]

    self.guardians: List[Person] = list(Person.select())
    self.guardian_combo["values"] = [""] + [guardian.name for guardian in self.guardians]
  
  def get_selected_id(self, combo: ttk.Combobox, records: List[Any]):
    index = combo.current()
    if index <= 0: return None
    return records[index - 1].id
  
  def get_form_data(self):
    return {
      "person_id": self.get_selected_id(self.person_combo, self.persons),
      "father_id": self.get_selected_id(self.father_combo, self.fathers),
      "mother_id": self.get_selected_id(self.mother_combo, self.mothers),
      "guardian_id": self.get_selected_id(self.guardian_combo, self.guardians),
    }

  def clear_form(self):
    self.person_combo.set("")
    self.father_combo.set("")
    self.mother_combo.set("")
    self.guardian_combo.set("")
