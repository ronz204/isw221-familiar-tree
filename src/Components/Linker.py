import tkinter as tk
from Enums.Colors import Colors

class Linker(tk.Button):
  def __init__(self, widget: tk.Widget, text: str):
    super().__init__(widget, **STYLES, text=text)

STYLES = {
  "cursor": "hand2",
  "highlightthickness": 0,
  "font": ("Arial", 12, "bold"),

  "bd": 0,
  "pady": 0,
  "padx": 12,
  "width": 20,
  "height": 2,
  "anchor": "w",

  "bg": Colors.GREEN_900.value,
  "fg": Colors.WHITE_100.value,
  "activebackground": Colors.GREEN_800.value,
  "activeforeground": Colors.WHITE_100.value,
}
