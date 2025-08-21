import tkinter as tk
from Enums.Colors import Colors

class Button(tk.Button):
  def __init__(self, widget: tk.Widget, text: str):
    super().__init__(widget, **STYLES, text=text)

    self.bind("<Enter>", self.on_hover)
    self.bind("<Leave>", self.on_leave)

  def on_hover(self, event: tk.Event):
    self.config(bg=Colors.GRAY_300.value)

  def on_leave(self, event: tk.Event):
    self.config(bg=Colors.GRAY_200.value)

STYLES = {
  "bd": 0,
  "relief": tk.FLAT,
  "cursor": "hand2",
  "font": ("Arial", 10, "bold"),
  "pady": 6,
  "padx": 12,
  "width": 20,
  "height": 2,
  "bg": Colors.GRAY_200.value,
  "fg": Colors.GRAY_800.value,
  "activebackground": Colors.GRAY_300.value,
}
