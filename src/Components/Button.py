import tkinter as tk
from Enums.Colors import Colors

class Button(tk.Button):
  def __init__(self, widget: tk.Widget, text: str):
    super().__init__(widget, **STYLES, text=text)
    self.bind("<Enter>", lambda e: self.configure(bg=Colors.GREEN_400.value))
    self.bind("<Leave>", lambda e: self.configure(bg=Colors.GREEN_300.value))

STYLES = {
  "font": ("Arial", 10, "bold"),
  "bg": Colors.GREEN_300.value,
  "fg": Colors.WHITE_100.value,
  "relief": tk.RAISED,
  "bd": 2,
  "cursor": "hand2",
  "width": 20,
  "height": 2
}