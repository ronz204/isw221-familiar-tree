import tkinter as tk
from Domain.Models.Person import Person
from typing import Any, Callable, Dict, List
from Presentation.Components.Combo import Combo
from Presentation.Components.Button import Button

class TimelineBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent: tk.Widget = parent

  def setup_grid(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)

  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid_rowconfigure(2, weight=1)
    self.container.grid(row=1, column=1, padx=30, pady=30, sticky=tk.NSEW)

  def build_frames(self):
    self.search_frame = tk.Frame(self.container)
    self.search_frame.grid(row=1, column=0, sticky=tk.EW, pady=(0, 20))
    self.search_frame.grid_columnconfigure(0, weight=1)
    self.search_frame.grid_columnconfigure(1, weight=1)
    
    self.main_content_frame = tk.Frame(self.container)
    self.main_content_frame.grid(row=2, column=0, sticky=tk.NSEW)
    self.main_content_frame.grid_columnconfigure(0, weight=1)
    self.main_content_frame.grid_columnconfigure(1, weight=2)
    self.main_content_frame.grid_rowconfigure(0, weight=1)
    
    self.info_frame = tk.Frame(self.main_content_frame)
    self.info_frame.grid(row=0, column=0, sticky=tk.NSEW, padx=(0, 10))
    self.info_frame.grid_columnconfigure(0, weight=1)
    self.info_frame.grid_columnconfigure(1, weight=1)
    
    self.timeline_frame = tk.Frame(self.main_content_frame)
    self.timeline_frame.grid(row=0, column=1, sticky=tk.NSEW, padx=(10, 0))
    self.timeline_frame.grid_columnconfigure(0, weight=1)
    self.timeline_frame.grid_rowconfigure(1, weight=1)

  def build_title(self):
    self.title = tk.Label(self.container, text="Línea de Tiempo", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, pady=(0, 25))

  def build_person_field(self):
    self.person_combo = Combo(self.search_frame, "Persona", [])
    self.person_combo.label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
    self.person_combo.combobox.grid(row=0, column=1, sticky=tk.EW, pady=(0, 12))

  def build_search_button(self, command: Callable):
    self.search_button = Button(self.search_frame, "Buscar", command=command)
    self.search_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

  def build_person_info_section(self):
    self.info_title = tk.Label(self.info_frame, text="Información Personal", font=("", 14, "bold"))
    self.info_title.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
    
    self.name_label = tk.Label(self.info_frame, text="Nombre: ", font=("", 10, "bold"))
    self.name_label.grid(row=1, column=0, sticky=tk.W, pady=2)
    self.name_value = tk.Label(self.info_frame, text="")
    self.name_value.grid(row=1, column=1, sticky=tk.W, pady=2)
    
    self.father_label = tk.Label(self.info_frame, text="Padre: ", font=("", 10, "bold"))
    self.father_label.grid(row=2, column=0, sticky=tk.W, pady=2)
    self.father_value = tk.Label(self.info_frame, text="")
    self.father_value.grid(row=2, column=1, sticky=tk.W, pady=2)
    
    self.mother_label = tk.Label(self.info_frame, text="Madre: ", font=("", 10, "bold"))
    self.mother_label.grid(row=3, column=0, sticky=tk.W, pady=2)
    self.mother_value = tk.Label(self.info_frame, text="")
    self.mother_value.grid(row=3, column=1, sticky=tk.W, pady=2)
    
    self.guard_label = tk.Label(self.info_frame, text="Guardián: ", font=("", 10, "bold"))
    self.guard_label.grid(row=4, column=0, sticky=tk.W, pady=2)
    self.guard_value = tk.Label(self.info_frame, text="")
    self.guard_value.grid(row=4, column=1, sticky=tk.W, pady=2)
    
    self.partner_label = tk.Label(self.info_frame, text="Pareja: ", font=("", 10, "bold"))
    self.partner_label.grid(row=5, column=0, sticky=tk.W, pady=2)
    self.partner_value = tk.Label(self.info_frame, text="")
    self.partner_value.grid(row=5, column=1, sticky=tk.W, pady=2)

  def build_timeline_section(self):
    self.timeline_title = tk.Label(self.timeline_frame, text="Eventos", font=("", 14, "bold"))
    self.timeline_title.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
    
    self.timeline_listbox_frame = tk.Frame(self.timeline_frame)
    self.timeline_listbox_frame.grid(row=1, column=0, sticky=tk.NSEW)
    self.timeline_listbox_frame.grid_columnconfigure(0, weight=1)
    self.timeline_listbox_frame.grid_rowconfigure(0, weight=1)
    
    self.timeline_listbox = tk.Listbox(self.timeline_listbox_frame)
    self.timeline_listbox.grid(row=0, column=0, sticky=tk.NSEW)
    
    self.timeline_scrollbar = tk.Scrollbar(self.timeline_listbox_frame, orient="vertical", command=self.timeline_listbox.yview)
    self.timeline_scrollbar.grid(row=0, column=1, sticky=tk.NS)
    self.timeline_listbox.configure(yscrollcommand=self.timeline_scrollbar.set)

  def load_data_hydration(self):
    self.persons: List[Person] = list(Person.select())
    person_names = [""] + [person.name for person in self.persons]
    self.person_combo.combobox["values"] = person_names

  def get_selected_id(self, combo_value: str, records: List[Person]):
    for person in records:
      if person.name == combo_value:
        return person.id
    return None

  def get_form_data(self) -> Dict[str, Any]:
    return {
      "person_id": self.get_selected_id(self.person_combo.combobox.get(), self.persons)
    }

  def clear_form_fields(self):
    self.person_combo.combobox.set("")
    self.clear_display_data()

  def clear_display_data(self):
    self.name_value.config(text="")
    self.father_value.config(text="")
    self.mother_value.config(text="")
    self.guard_value.config(text="")
    self.partner_value.config(text="")
    self.timeline_listbox.delete(0, tk.END)

  def display_person_info(self, data: Dict[str, Any]):
    person = data.get("person")
    father = data.get("father")
    mother = data.get("mother")
    guard = data.get("guard")
    partner = data.get("partner")
    
    self.name_value.config(text=person.name if person else "")
    self.father_value.config(text=father.name if father else "No registrado")
    self.mother_value.config(text=mother.name if mother else "No registrado")
    self.guard_value.config(text=guard.name if guard else "No registrado")
    self.partner_value.config(text=partner.name if partner else "No registrado")

  def display_timeline(self, timeline_events: List[Dict[str, Any]]):
    self.timeline_listbox.delete(0, tk.END)
    
    if not timeline_events:
      self.timeline_listbox.insert(tk.END, "No hay eventos registrados")
    else:
      for event in timeline_events:
        event_text = f"{event['timestamp']} - {event['label']}"
        self.timeline_listbox.insert(tk.END, event_text)