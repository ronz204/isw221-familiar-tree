import tkinter as tk
from Enums.Colors import Colors

class Label(tk.Label):
  def __init__(self, widget: tk.Widget, text: str):
    super().__init__(widget, **STYLES, text=text)

STYLES = {
  "anchor": "w",
  "justify": "left",
  "font": ("Arial", 10,  "bold"),
  "bg": Colors.WHITE_100.value,
  "fg": Colors.GRAY_800.value,
}
