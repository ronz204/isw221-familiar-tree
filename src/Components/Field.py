import tkinter as tk
from Enums.Colors import Colors

class Field(tk.Entry):
  def __init__(self, widget: tk.Widget, width: int = 25):
    super().__init__(widget, **STYLES, width=width)

STYLES = {
  "font": ("Arial", 10),
  "relief": tk.RIDGE,
  "bd": 1
}
