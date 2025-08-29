import tkinter as tk
from tkinter import ttk
from typing import Callable, List, Dict, Any

class DeceasedPeopleScreenBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent = parent
    self.deceased_people: List[Dict[str, Any]] = []

  def build_layout(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)
  
  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid_rowconfigure(2, weight=1)
    self.container.grid(row=1, column=1, padx=40, pady=40, sticky="nsew")

  def build_title(self):
    self.title = tk.Label(self.container, text="Personas que fallecieron antes de los 50 años", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=2, pady=(0, 25))

  def build_frames(self):
    self.button_frame = tk.Frame(self.container)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 20))

    self.result_frame = tk.Frame(self.container)
    self.result_frame.grid_columnconfigure(0, weight=1)
    self.result_frame.grid_rowconfigure(1, weight=1)
    self.result_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

  def build_search_button(self, command: Callable):
    self.search_button = tk.Button(self.button_frame, text="Buscar Personas Fallecidas", command=command)
    self.search_button.config(width=25, height=2, font=("", 11, "bold"))
    self.search_button.grid(row=0, column=0, pady=(0, 10))

  def build_result_area(self):
    self.result_title = tk.Label(self.result_frame, text="Resultados:", font=("", 12, "bold"))
    self.result_title.grid(row=0, column=0, sticky="w", pady=(0, 10))
    
    self.listbox_frame = tk.Frame(self.result_frame)
    self.listbox_frame.grid_columnconfigure(0, weight=1)
    self.listbox_frame.grid_rowconfigure(0, weight=1)
    self.listbox_frame.grid(row=1, column=0, sticky="nsew")
    
    self.result_listbox = tk.Listbox(self.listbox_frame, font=("", 10), height=20)
    self.result_listbox.grid(row=0, column=0, sticky="nsew")
    
    self.scrollbar = ttk.Scrollbar(self.listbox_frame, orient="vertical", command=self.result_listbox.yview)
    self.scrollbar.grid(row=0, column=1, sticky="ns")
    self.result_listbox.config(yscrollcommand=self.scrollbar.set)
    
    self.h_scrollbar = ttk.Scrollbar(self.listbox_frame, orient="horizontal", command=self.result_listbox.xview)
    self.h_scrollbar.grid(row=1, column=0, sticky="ew")
    self.result_listbox.config(xscrollcommand=self.h_scrollbar.set)

  def build_info_label(self):
    self.info_label = tk.Label(self.result_frame, text="Presiona 'Buscar Personas Fallecidas' para mostrar los resultados", font=("", 10), fg="gray")
    self.info_label.grid(row=2, column=0, sticky="w", pady=(10, 0))

  def populate_results(self, deceased_people: List[Dict[str, Any]]):
    self.result_listbox.delete(0, tk.END)
    self.deceased_people = deceased_people
    
    if not deceased_people:
      self.result_listbox.insert(tk.END, "No se encontraron personas que fallecieron antes de los 50 años")
      self.info_label.config(text="No hay resultados para mostrar", fg="orange")
      return
    
    for person in deceased_people:
      info = f"ID: {person['id']} | {person['name']} | Cédula: {person['cedula']} | Edad al morir: {person['age_at_death']} años | Fecha defunción: {person['deathdate']}"
      self.result_listbox.insert(tk.END, info)
    
    count = len(deceased_people)
    self.info_label.config(text=f"Se encontraron {count} persona(s) que fallecieron antes de los 50 años", fg="green")

  def clear_results(self):
    self.result_listbox.delete(0, tk.END)
    self.deceased_people = []
    self.info_label.config(text="Presiona 'Buscar Personas Fallecidas' para mostrar los resultados", fg="gray")
