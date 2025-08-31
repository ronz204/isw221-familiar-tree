import tkinter as tk

class Field:
  def __init__(self, parent: tk.Widget, label: str):
    self.parent: tk.Widget = parent

    self.label = tk.Label(self.parent, text=label)
    self.entry = tk.Entry(self.parent, font=("", 10))
