import tkinter as tk
from Enums.Colors import Colors

class Field(tk.Entry):
  def __init__(self, widget: tk.Widget, width: int = 25):
    super().__init__(widget, **STYLES, width=width)
    
    self.bind("<Enter>", self.on_hover)
    self.bind("<Leave>", self.on_leave)

  def on_hover(self, event: tk.Event):
    if not self.focus_get() == self:
      self.config(bg=Colors.GRAY_50.value)

  def on_leave(self, event: tk.Event):
    if not self.focus_get() == self:
      self.config(bg=Colors.WHITE_100.value)

STYLES = {
  "bd": 1,
  "relief": tk.RIDGE,
  "font": ("Arial", 10),
  "fg": Colors.GRAY_800.value,
  "bg": Colors.WHITE_100.value,
  "insertbackground": Colors.BLUE_500.value,
  "selectbackground": Colors.BLUE_200.value,
  "selectforeground": Colors.GRAY_900.value
}
