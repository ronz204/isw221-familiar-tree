import tkinter as tk
import datetime as dt
from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from typing import Any, Callable, Dict, List
from Presentation.Components.Field import Field
from Presentation.Components.Combo import Combo
from Presentation.Components.Button import Button

class MatchBuilder:
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
    self.title = tk.Label(self.container, text="Emparejar Personas", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=3, pady=(0, 25))

  def build_man_field(self):
    self.man_combo = Combo(self.form_frame, "Hombre", [])
    self.man_combo.label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
    self.man_combo.combobox.grid(row=1, column=1, sticky=tk.EW, pady=(0, 12))

  def build_woman_field(self):
    self.woman_combo = Combo(self.form_frame, "Mujer", [])
    self.woman_combo.label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
    self.woman_combo.combobox.grid(row=2, column=1, sticky=tk.EW, pady=(0, 12))

  def build_timestamp_field(self):
    self.timestamp_field = Field(self.form_frame, "Fecha")
    self.timestamp_field.label.grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
    self.timestamp_field.entry.grid(row=3, column=1, sticky=tk.EW, pady=(0, 12))
    
    current_date = dt.datetime.now().strftime("%Y-%m-%d")
    self.timestamp_field.entry.insert(0, current_date)

  def build_relate_button(self, command: Callable):
    self.relate_button = Button(self.buttons_frame, "Emparejar", command=command)
    self.relate_button.grid(row=0, column=0, pady=(10, 0))

  def build_discard_button(self, command: Callable):
    self.discard_button = Button(self.buttons_frame, "Cancelar", command=command)
    self.discard_button.grid(row=0, column=1, pady=(10, 0))

  def load_data_hydration(self):
    emotional_predicate = Person.emotional >= 70
    status_predicate = ((Person.status == Status.SINGLE.value) | (Person.status == Status.WIDOWED.value) | (Person.status == Status.DEATHED.value))

    self.men: List[Person] = list(Person.select().where(
      (Person.gender == "M") & emotional_predicate & status_predicate
    ))

    self.women: List[Person] = list(Person.select().where(
      (Person.gender == "F") & emotional_predicate & status_predicate
    ))

    men_names = [""] + [man.name for man in self.men]
    women_names = [""] + [woman.name for woman in self.women]
    
    self.man_combo.combobox["values"] = men_names
    self.woman_combo.combobox["values"] = women_names

  def get_selected_id(self, combo_value: str, records: List[Person]):
    for person in records:
      if person.name == combo_value:
        return person.id
    return None

  def get_form_data(self) -> Dict[str, Any]:
    return {
      "man_id": self.get_selected_id(self.man_combo.combobox.get(), self.men),
      "woman_id": self.get_selected_id(self.woman_combo.combobox.get(), self.women),
      "timestamp": self.timestamp_field.entry.get().strip()
    }

  def clear_form_fields(self):
    self.man_combo.combobox.set("")
    self.woman_combo.combobox.set("")
    self.timestamp_field.entry.delete(0, tk.END)

    current_date = dt.datetime.now().strftime("%Y-%m-%d")
    self.timestamp_field.entry.insert(0, current_date)
