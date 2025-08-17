import tkinter as tk
from Enums.Pallete import Pallete

class TabNav(tk.Button):
  def __init__(self, widget: tk.Widget, text: str):
    super().__init__(widget, text=text, **STYLES)

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

  "bg": Pallete.GREEN_200.value,
  "fg": Pallete.WHITE_100.value,
  "activebackground": Pallete.GREEN_100.value,
  "activeforeground": Pallete.WHITE_100.value,
}