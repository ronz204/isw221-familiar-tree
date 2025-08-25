import tkinter as tk
from tkinter import ttk
from Models.Person import Person
from typing import Callable, List

class RelateScreenBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent = parent

    self.people: List[Person] = []

  def build_layout(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)
  
  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid(row=1, column=1, padx=40, pady=40)

  def build_title(self):
    self.title = tk.Label(self.container, text="Relacionar Personas", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=2, pady=(0, 25))

  def build_frames(self):
    self.form_frame = tk.Frame(self.container)
    self.form_frame.grid_columnconfigure(0, weight=1)
    self.form_frame.grid_columnconfigure(1, weight=1)
    self.form_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(0, 20))

    self.button_frame = tk.Frame(self.container)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(1, weight=1)
    self.button_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

  def build_person1_field(self):
    self.person1_label = tk.Label(self.form_frame, text="Primera Persona:")
    self.person1_label.grid(row=0, column=0, sticky="w", pady=(0, 5), padx=(0, 10))
    self.person1_combo = ttk.Combobox(self.form_frame, state="readonly", width=25)
    self.person1_combo.grid(row=1, column=0, sticky="ew", pady=(0, 15), padx=(0, 10))

  def build_person2_field(self):
    self.person2_label = tk.Label(self.form_frame, text="Segunda Persona:")
    self.person2_label.grid(row=0, column=1, sticky="w", pady=(0, 5), padx=(10, 0))
    self.person2_combo = ttk.Combobox(self.form_frame, state="readonly", width=25)
    self.person2_combo.grid(row=1, column=1, sticky="ew", pady=(0, 15), padx=(10, 0))

  def build_relate_button(self, command: Callable):
    self.relate_button = tk.Button(self.button_frame, text="Relacionar", command=command)
    self.relate_button.config(width=15, height=2, font=("", 11, "bold"))
    self.relate_button.grid(row=0, column=0, padx=(0, 10), sticky="e")

  def build_discard_button(self, command: Callable):
    self.discard_button = tk.Button(self.button_frame, text="Cancelar", command=command)
    self.discard_button.config(width=15, height=2, font=("", 11, "bold"))
    self.discard_button.grid(row=0, column=1, padx=(10, 0), sticky="w")

  def load_data_hydration(self):
    self.people = list(Person.select().where(Person.couple.is_null()))
    person_names = [f"{person.name}" for person in self.people]
    
    self.person1_combo["values"] = [""] + person_names
    self.person2_combo["values"] = [""] + person_names

  def get_selected_id(self, combo: ttk.Combobox):
    index = combo.current()
    if index <= 0: return None
    return self.people[index - 1].id
  
  def get_form_data(self):
    return {
      "person1_id": self.get_selected_id(self.person1_combo),
      "person2_id": self.get_selected_id(self.person2_combo),
    }
  
  def clear_form(self):
    self.person1_combo.set("")
    self.person2_combo.set("")
