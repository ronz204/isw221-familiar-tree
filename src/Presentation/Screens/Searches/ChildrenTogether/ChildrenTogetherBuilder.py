import tkinter as tk
from tkinter import ttk
from typing import Any, Callable, Dict, List
from Presentation.Components.Button import Button

class ChildrenTogetherBuilder:
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
    self.container.grid(row=1, column=1, padx=40, pady=40, sticky=tk.NSEW)

  def build_title(self):
    self.title = tk.Label(self.container, text="Parejas con Hijos", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, pady=(0, 25))

  def build_frames(self):
    self.button_frame = tk.Frame(self.container)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid(row=1, column=0, sticky=tk.EW, pady=(0, 20))

    self.result_frame = tk.Frame(self.container)
    self.result_frame.grid_columnconfigure(0, weight=1)
    self.result_frame.grid_rowconfigure(1, weight=1)
    self.result_frame.grid(row=2, column=0, sticky=tk.NSEW)

  def build_search_button(self, command: Callable):
    self.search_button = Button(self.button_frame, "Buscar Parejas con Hijos", command)
    self.search_button.config(width=25, height=2, font=("", 11, "bold"))
    self.search_button.grid(row=0, column=0)

  def build_result_section(self):
    self.result_title = tk.Label(self.result_frame, text="Resultados:", font=("", 12, "bold"))
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
    self.info_label = tk.Label(self.result_frame, text="Presiona 'Buscar Parejas con Hijos' para mostrar los resultados", font=("", 10), fg="gray")
    self.info_label.grid(row=2, column=0, sticky=tk.W, pady=(10, 0))

  def display_results(self, couples: List[Dict[str, Any]]):
    self.result_listbox.delete(0, tk.END)
    
    if not couples:
      self.result_listbox.insert(tk.END, "No se encontraron parejas con hijos.")
      self.info_label.config(text="No hay resultados para mostrar", fg="orange")
      return
    
    for couple in couples:
      info = f"{couple['man_name']} & {couple['woman_name']} | {couple['children_count']} hijos en común"
      self.result_listbox.insert(tk.END, info)
    
    count = len(couples)
    self.info_label.config(text=f"Se encontraron {count} pareja(s) con 2 o más hijos en común", fg="green")

  def clear_results(self):
    self.result_listbox.delete(0, tk.END)
    self.info_label.config(text="Presiona 'Buscar Parejas con Hijos' para mostrar los resultados", fg="gray")
