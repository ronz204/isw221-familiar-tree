import tkinter as tk
from tkinter import ttk
from typing import List

class Combo():
  def __init__(self, parent: tk.Widget, label: str, values: List[str]):
    self.parent: tk.Widget = parent

    self.label = tk.Label(parent, text=label)
    self.combobox = ttk.Combobox(parent, values=values, state="readonly")
