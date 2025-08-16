import tkinter as tk
from Components.Navigation import Navigation

class DashView(tk.Frame):
  def __init__(self, widget: tk.Widget):
    super().__init__(widget)
    self.setup()

  def setup(self) -> None:
    navigation = Navigation(self)
    navigation.pack(side=tk.LEFT, fill=tk.Y)
