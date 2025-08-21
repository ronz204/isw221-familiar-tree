import tkinter as tk
from Enums.Colors import Colors

class Label(tk.Label):
  def __init__(self, widget: tk.Widget, text: str):
    super().__init__(widget, **STYLES, text=text)

STYLES = {
  "font": ("Arial", 10),
  "bg": Colors.GRAY_100.value,
  "fg": Colors.GRAY_200.value
}