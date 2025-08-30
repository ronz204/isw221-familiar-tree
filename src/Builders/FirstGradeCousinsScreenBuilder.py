import tkinter as tk
from tkinter import ttk
from Models.Person import Person
from typing import Callable, List

class FirstGradeCousinsScreenBuilder:
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
    self.title = tk.Label(self.container, text="Primos de Primer Grado", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=2, pady=(0, 25))

  def build_frames(self):
    self.form_frame = tk.Frame(self.container)
    self.form_frame.grid_columnconfigure(0, weight=1)
    self.form_frame.grid_columnconfigure(1, weight=1)
    self.form_frame.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(0, 20))

    self.result_frame = tk.Frame(self.container)
    self.result_frame.grid_columnconfigure(0, weight=1)
    self.result_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 20))

    self.button_frame = tk.Frame(self.container)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid(row=3, column=0, columnspan=2, sticky="ew")

  def build_person_field(self):
    self.person_label = tk.Label(self.form_frame, text="Seleccionar Persona:")
    self.person_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
    self.person_combo = ttk.Combobox(self.form_frame, state="readonly", width=30)
    self.person_combo.grid(row=1, column=0, sticky="ew", pady=(0, 15))

  def build_result_list(self):
    self.result_title = tk.Label(self.result_frame, text="Primos de Primer Grado:", font=("", 12, "bold"))
    self.result_title.grid(row=0, column=0, sticky="w", pady=(0, 5))
    
    self.listbox_frame = tk.Frame(self.result_frame)
    self.listbox_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
    self.listbox_frame.grid_columnconfigure(0, weight=1)
    
    self.cousins_listbox = tk.Listbox(self.listbox_frame, height=8, font=("", 10))
    self.cousins_listbox.grid(row=0, column=0, sticky="ew")
    
    self.scrollbar = tk.Scrollbar(self.listbox_frame, orient="vertical")
    self.scrollbar.grid(row=0, column=1, sticky="ns")
    
    self.cousins_listbox.config(yscrollcommand=self.scrollbar.set)
    self.scrollbar.config(command=self.cousins_listbox.yview)
    
    self.cousins_listbox.insert(0, "Selecciona una persona y presiona 'Buscar Primos'")
    self.cousins_listbox.config(state="disabled")

  def build_search_button(self, command: Callable):
    self.search_button = tk.Button(self.button_frame, text="Buscar Primos", command=command)
    self.search_button.config(width=20, height=2, font=("", 11, "bold"))
    self.search_button.grid(row=0, column=0, padx=(0, 10), sticky="e")

  def build_clear_button(self, command: Callable):
    self.clear_button = tk.Button(self.button_frame, text="Limpiar", command=command)
    self.clear_button.config(width=15, height=2, font=("", 11, "bold"))
    self.clear_button.grid(row=0, column=1, padx=(10, 0), sticky="w")

  def load_data_hydration(self):
    self.people = list(Person.select())
    people_names = [f"{person.name}" for person in self.people]
    
    self.person_combo["values"] = [""] + people_names

  def get_selected_id(self):
    index = self.person_combo.current()
    if index <= 0: return None
    return self.people[index - 1].id
  
  def get_form_data(self):
    return {
      "person_id": self.get_selected_id()
    }
  
  def clear_form(self):
    self.person_combo.set("")
    self.clear_results()

  def clear_results(self):
    self.cousins_listbox.config(state="normal")
    self.cousins_listbox.delete(0, tk.END)
    self.cousins_listbox.insert(0, "Selecciona una persona y presiona 'Buscar Primos'")
    self.cousins_listbox.config(state="disabled")

  def set_cousins_result(self, cousins: List[Person], person_name: str):
    self.cousins_listbox.config(state="normal")
    self.cousins_listbox.delete(0, tk.END)
    
    if cousins:
      self.cousins_listbox.insert(0, f"Primos de {person_name}:")
      self.cousins_listbox.insert(1, "─" * 40)
      
      for i, cousin in enumerate(cousins, 3):
        self.cousins_listbox.insert(i, f"• {cousin.name} (ID: {cousin.id})")
      
      self.cousins_listbox.insert(len(cousins) + 3, "")
      self.cousins_listbox.insert(len(cousins) + 4, f"Total: {len(cousins)} primo(s) encontrado(s)")
    else:
      self.cousins_listbox.insert(0, f"{person_name} no tiene primos de primer grado")
    
    self.cousins_listbox.config(state="disabled")