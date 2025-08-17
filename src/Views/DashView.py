import tkinter as tk
from Views.BaseView import BaseView
from Components.Navigation import Navigation

class DashView(BaseView):
  def __init__(self, parent: tk.Widget):
    super().__init__(parent)
    self.setup()

  def setup(self) -> None:
    navigation = Navigation(self)
    navigation.pack(side=tk.LEFT, fill=tk.Y)
