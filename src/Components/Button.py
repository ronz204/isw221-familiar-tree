import tkinter as tk
from typing import Callable

class Button(tk.Button):
  def __init__(self, parent: tk.Widget, text: str, command: Callable):
    super().__init__(parent, text=text, command=command)
    self.config(width=12, height=2, font=("", 11, "bold"))
