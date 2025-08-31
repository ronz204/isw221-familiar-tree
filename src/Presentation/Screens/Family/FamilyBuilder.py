import tkinter as tk
from tkinter import ttk
from typing import List
from Domain.Models.Person import Person
from Presentation.Components.Node import Node
from Presentation.Components.Edge import Edge

class FamilyBuilder:
  def __init__(self, parent: tk.Widget, go_back_command=None):
    self.parent = parent
    self.people: List[Person] = []

  def setup_grid(self):
    self.parent.grid_rowconfigure(0, weight=1)
    self.parent.grid_columnconfigure(0, weight=1)

  def build_title(self):
    self.title = tk.Label(self.parent, text="Árbol Genealógico", font=("Arial", 16, "bold"))
    self.title.pack(pady=10)

  def build_canvas(self):
    self.canvas_frame = tk.Frame(self.parent)
    self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

  def build_scrollers(self):
    self.canvas = tk.Canvas(self.canvas_frame, bg="white")
    self.v_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
    self.h_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)

    self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

    self.canvas.grid(row=0, column=0, sticky="nsew")
    self.v_scroll.grid(row=0, column=1, sticky="ns")
    self.h_scroll.grid(row=1, column=0, sticky="ew")
    self.canvas_frame.grid_rowconfigure(0, weight=1)
    self.canvas_frame.grid_columnconfigure(0, weight=1)

  def load_data_hydration(self):
    self.people = list(Person.select())
