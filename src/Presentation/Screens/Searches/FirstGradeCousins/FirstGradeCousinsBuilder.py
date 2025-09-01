import tkinter as tk
from tkinter import ttk
from Domain.Models.Person import Person
from typing import Any, Callable, Dict, List
from Presentation.Components.Combo import Combo
from Presentation.Components.Button import Button

class FirstGradeCousinsBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent: tk.Widget = parent

  def setup_grid(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)

  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid_rowconfigure(3, weight=1)
    self.container.grid(row=1, column=1, padx=40, pady=40, sticky=tk.NSEW)

  def build_title(self):
    self.title = tk.Label(self.container, text="Buscar Primos Hermanos", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, pady=(0, 25))

  def build_frames(self):
    self.form_frame = tk.Frame(self.container)
    self.form_frame.grid_columnconfigure(0, weight=1)
    self.form_frame.grid(row=1, column=0, sticky=tk.EW, pady=(0, 20))

    self.button_frame = tk.Frame(self.container)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(1, weight=1)
    self.button_frame.grid(row=2, column=0, sticky=tk.EW, pady=(0, 20))

    self.result_frame = tk.Frame(self.container)
    self.result_frame.grid_columnconfigure(0, weight=1)
    self.result_frame.grid_rowconfigure(1, weight=1)
    self.result_frame.grid(row=3, column=0, sticky=tk.NSEW)

  def build_person_field(self):
    self.person_combo = Combo(self.form_frame, "Seleccionar Persona", [])
    self.person_combo.label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
    self.person_combo.combobox.grid(row=1, column=0, sticky=tk.EW, pady=(0, 15))

  def build_search_button(self, command: Callable):
    self.search_button = Button(self.button_frame, "Buscar Primos", command)
    self.search_button.config(width=20, height=2, font=("", 11, "bold"))
    self.search_button.grid(row=0, column=0, padx=(0, 10), sticky=tk.E)

  def build_clear_button(self, command: Callable):
    self.clear_button = Button(self.button_frame, "Limpiar", command)
    self.clear_button.config(width=15, height=2, font=("", 11, "bold"))
    self.clear_button.grid(row=0, column=1, padx=(10, 0), sticky=tk.W)

  def build_result_section(self):
    self.result_title = tk.Label(self.result_frame, text="Primos Hermanos:", font=("", 12, "bold"))
    self.result_title.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
    
    self.listbox_frame = tk.Frame(self.result_frame)
    self.listbox_frame.grid_columnconfigure(0, weight=1)
    self.listbox_frame.grid_rowconfigure(0, weight=1)
    self.listbox_frame.grid(row=1, column=0, sticky=tk.NSEW)
    
    self.result_listbox = tk.Listbox(self.listbox_frame, font=("", 10), height=20)
    self.result_listbox.grid(row=0, column=0, sticky=tk.NSEW)
    
    self.scrollbar = ttk.Scrollbar(self.listbox_frame, orient="vertical", command=self.result_listbox.yview)
    self.scrollbar.grid(row=0, column=1, sticky=tk.NS)
    self.result_listbox.config(yscrollcommand=self.scrollbar.set)

  def build_info_label(self):
    self.info_label = tk.Label(self.result_frame, text="Selecciona una persona y presiona 'Buscar Primos'", 
                              font=("", 10), fg="gray")
    self.info_label.grid(row=2, column=0, sticky=tk.W, pady=(10, 0))

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
    self.clear_results()

  def display_results(self, cousins: List[Person], selected_person_name: str):
    self.result_listbox.delete(0, tk.END)
    
    if not cousins:
      self.result_listbox.insert(tk.END, f"No se encontraron primos hermanos para {selected_person_name}")
      self.info_label.config(text="No hay primos hermanos para mostrar", fg="orange")
      return
    
    for cousin in cousins:
      info = f"{cousin.name} (ID: {cousin.cedula}) | Edad: {cousin.age} años"
      self.result_listbox.insert(tk.END, info)
    
    count = len(cousins)
    self.info_label.config(text=f"Se encontraron {count} primo(s) hermano(s) de {selected_person_name}", fg="green")

  def clear_results(self):
    self.result_listbox.delete(0, tk.END)
    self.info_label.config(text="Selecciona una persona y presiona 'Buscar Primos'", fg="gray")
