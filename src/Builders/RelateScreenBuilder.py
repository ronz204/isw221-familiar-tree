import tkinter as tk
import datetime as dt
from tkinter import ttk
from Models.Person import Person
from Models.Enums.Status import Status
from typing import Callable, List, Any

class RelateScreenBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent = parent

    self.men: List[Person] = []
    self.women: List[Person] = []

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

  def build_man_field(self):
    self.man_label = tk.Label(self.form_frame, text="Hombre:")
    self.man_label.grid(row=0, column=0, sticky="w", pady=(0, 5), padx=(0, 10))
    self.man_combo = ttk.Combobox(self.form_frame, state="readonly", width=25)
    self.man_combo.grid(row=1, column=0, sticky="ew", pady=(0, 15), padx=(0, 10))

  def build_woman_field(self):
    self.woman_label = tk.Label(self.form_frame, text="Mujer:")
    self.woman_label.grid(row=0, column=1, sticky="w", pady=(0, 5), padx=(10, 0))
    self.woman_combo = ttk.Combobox(self.form_frame, state="readonly", width=25)
    self.woman_combo.grid(row=1, column=1, sticky="ew", pady=(0, 15), padx=(10, 0))

  def build_year_field(self):
    self.year_label = tk.Label(self.form_frame, text="Año de la relación:")
    self.year_label.grid(row=2, column=0, sticky="w", pady=(0, 5), padx=(0, 10))
    self.year_entry = tk.Entry(self.form_frame, width=25)
    self.year_entry.grid(row=3, column=0, sticky="ew", pady=(0, 15), padx=(0, 10))
    self.year_entry.insert(0, str(dt.datetime.now().year))

  def build_relate_button(self, command: Callable):
    self.relate_button = tk.Button(self.button_frame, text="Relacionar", command=command)
    self.relate_button.config(width=15, height=2, font=("", 11, "bold"))
    self.relate_button.grid(row=0, column=0, padx=(0, 10), sticky="e")

  def build_discard_button(self, command: Callable):
    self.discard_button = tk.Button(self.button_frame, text="Cancelar", command=command)
    self.discard_button.config(width=15, height=2, font=("", 11, "bold"))
    self.discard_button.grid(row=0, column=1, padx=(10, 0), sticky="w")

  def load_data_hydration(self):
    emotional_predicate = Person.emotional >= 70
    deathdate_predicate = Person.deathdate.is_null()
    status_predicate = ((Person.status == Status.SINGLE.value) | (Person.status == Status.WIDOWED.value))

    self.men = list(Person.select().where(
      (Person.gender == "M") & emotional_predicate & deathdate_predicate & status_predicate
    ))

    self.women = list(Person.select().where(
      (Person.gender == "F")  & emotional_predicate & deathdate_predicate & status_predicate
    ))

    men_names = [f"{man.name}" for man in self.men]
    women_names = [f"{woman.name}" for woman in self.women]
    
    self.man_combo["values"] = [""] + men_names
    self.woman_combo["values"] = [""] + women_names

  def get_selected_id(self, combo: ttk.Combobox, records: List[Any]):
    index = combo.current()
    if index <= 0: return None
    return records[index - 1].id
  
  def get_form_data(self):
    return {
      "man_id": self.get_selected_id(self.man_combo, self.men),
      "woman_id": self.get_selected_id(self.woman_combo, self.women),
      "year": int(self.year_entry.get().strip())
    }
  
  def clear_form(self):
    self.man_combo.set("")
    self.woman_combo.set("")
    self.year_entry.delete(0, tk.END)
    self.year_entry.insert(0, str(dt.datetime.now().year))
