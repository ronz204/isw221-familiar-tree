import tkinter as tk
from typing import Callable

class FamilyScreenBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent = parent

  def build_layout(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)
  
  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid(row=1, column=1, padx=40, pady=40)
  
  def build_frames(self):
    self.button_frame = tk.Frame(self.container)
    self.button_frame.config(bd=2, padx=15, pady=15)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(1, weight=1)
    self.button_frame.grid(row=3, column=0, columnspan=2, sticky="ew")

  def build_title(self):
    self.title_label = tk.Label(self.container, text="Registrar Familia", font=("Helvetica", 16))
    self.title_label.grid(row=0, column=0, pady=10)
  
  def build_name_field(self):
    self.name_label = tk.Label(self.container, text="Nombre de la familia:")
    self.name_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))
    self.name_entry = tk.Entry(self.container, font=("", 12), width=40)
    self.name_entry.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 30))
  
  def build_save_button(self, command: Callable):
    self.save_button = tk.Button(self.button_frame, text="Save", command=command)
    self.save_button.config(width=15, height=2, font=("", 10, "bold"))
    self.save_button.grid(row=0, column=0, padx=(0, 10), sticky="e")

  def build_discard_button(self, command: Callable):
    self.discard_button = tk.Button(self.button_frame, text="Discard", command=command)
    self.discard_button.config(width=15, height=2, font=("", 10, "bold"))
    self.discard_button.grid(row=0, column=1, padx=(10, 0), sticky="w")
