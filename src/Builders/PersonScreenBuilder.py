import tkinter as tk
from tkinter import ttk
from Models.Person import Person
from Models.Family import Family
from typing import Callable, List

class PersonScreenBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent = parent

    self.mothers: List[Person] = []
    self.fathers: List[Person] = []
    self.families: List[Family] = []

  def build_layout(self):
    for index in range(3):
      self.parent.grid_rowconfigure(index, weight=1)
      self.parent.grid_columnconfigure(index, weight=1)

  def build_container(self):
    self.container = tk.Frame(self.parent)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid_columnconfigure(1, weight=1)
    self.container.grid_columnconfigure(2, weight=1)
    self.container.grid(row=1, column=1, padx=30, pady=30)

  def build_title(self):
    self.title = tk.Label(self.container, text="Registrar Persona", font=("", 16, "bold"))
    self.title.grid(row=0, column=0, columnspan=3, pady=(0, 25))

  def build_frames(self):
    self.left_frame = tk.Frame(self.container)
    self.left_frame.grid_columnconfigure(0, weight=1)
    self.left_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 15))
    
    self.center_frame = tk.Frame(self.container)
    self.center_frame.grid_columnconfigure(0, weight=1)
    self.center_frame.grid(row=1, column=1, sticky="nsew", padx=(15, 15))

    self.right_frame = tk.Frame(self.container)
    self.right_frame.grid_columnconfigure(0, weight=1)
    self.right_frame.grid(row=1, column=2, sticky="nsew", padx=(15, 0))

  def build_name_field(self):
    self.name_label = tk.Label(self.left_frame, text="Nombre:")
    self.name_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
    self.name_entry = tk.Entry(self.left_frame, font=("", 10), width=20)
    self.name_entry.grid(row=2, column=0, sticky="ew", pady=(0, 12))

  def build_cedula_field(self):
    self.cedula_label = tk.Label(self.left_frame, text="Cédula:")
    self.cedula_label.grid(row=3, column=0, sticky="w", pady=(0, 5))
    self.cedula_entry = tk.Entry(self.left_frame, font=("", 10), width=20)
    self.cedula_entry.grid(row=4, column=0, sticky="ew", pady=(0, 12))

  def build_province_field(self):
    self.province_label = tk.Label(self.left_frame, text="Provincia:")
    self.province_label.grid(row=5, column=0, sticky="w", pady=(0, 5))
    self.province_entry = tk.Entry(self.left_frame, font=("", 10), width=20)
    self.province_entry.grid(row=6, column=0, sticky="ew", pady=(0, 12))

  def build_age_field(self):
    self.age_label = tk.Label(self.left_frame, text="Edad:")
    self.age_label.grid(row=7, column=0, sticky="w", pady=(0, 5))
    self.age_entry = tk.Entry(self.left_frame, font=("", 10), width=20)
    self.age_entry.grid(row=8, column=0, sticky="ew", pady=(0, 12))

  def build_birthdate_field(self):
    self.birthdate_label = tk.Label(self.left_frame, text="Fecha nacimiento:")
    self.birthdate_label.grid(row=9, column=0, sticky="w", pady=(0, 5))
    self.birthdate_entry = tk.Entry(self.left_frame, font=("", 10), width=20)
    self.birthdate_entry.grid(row=10, column=0, sticky="ew", pady=(0, 12))

  def build_emotional_field(self):
    self.emotional_label = tk.Label(self.left_frame, text="Estado emocional:")
    self.emotional_label.grid(row=11, column=0, sticky="w", pady=(0, 5))
    self.emotional_entry = tk.Entry(self.left_frame, font=("", 10), width=20)
    self.emotional_entry.insert(0, "100")
    self.emotional_entry.grid(row=12, column=0, sticky="ew", pady=(0, 12))

  def build_gender_field(self):
    self.gender_label = tk.Label(self.center_frame, text="Género:")
    self.gender_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
    self.gender_var = tk.StringVar()
    self.gender_combo = ttk.Combobox(self.center_frame, textvariable=self.gender_var, values=["M", "F"], state="readonly", width=18)
    self.gender_combo.grid(row=2, column=0, sticky="ew", pady=(0, 12))

  def build_family_field(self):
    self.family_label = tk.Label(self.center_frame, text="Familia:")
    self.family_label.grid(row=3, column=0, sticky="w", pady=(0, 5))
    self.family_combo = ttk.Combobox(self.center_frame, state="readonly", width=18)
    self.family_combo.grid(row=4, column=0, sticky="ew", pady=(0, 12))

  def build_father_field(self):
    self.father_label = tk.Label(self.center_frame, text="Padre:")
    self.father_label.grid(row=5, column=0, sticky="w", pady=(0, 5))
    self.father_combo = ttk.Combobox(self.center_frame, state="readonly", width=18)
    self.father_combo.grid(row=6, column=0, sticky="ew", pady=(0, 12))

  def build_mother_field(self):
    self.mother_label = tk.Label(self.center_frame, text="Madre:")
    self.mother_label.grid(row=7, column=0, sticky="w", pady=(0, 5))
    self.mother_combo = ttk.Combobox(self.center_frame, state="readonly", width=18)
    self.mother_combo.grid(row=8, column=0, sticky="ew", pady=(0, 12))

  def build_save_button(self, command: Callable):
    self.save_button = tk.Button(self.right_frame, text="Save", command=command)
    self.save_button.config(width=12, height=2, font=("", 11, "bold"))
    self.save_button.grid(row=1, column=0, pady=(0, 15))

  def build_discard_button(self, command: Callable):
    self.discard_button = tk.Button(self.right_frame, text="Discard", command=command)
    self.discard_button.config(width=12, height=2, font=("", 11, "bold"))
    self.discard_button.grid(row=2, column=0)
