import tkinter as tk
from Views.BaseView import BaseView

class MemberView(BaseView):
  def __init__(self, widget: tk.Widget):
    super().__init__(widget)
    self.render()

  def render(self) -> None:
    self.lbl_testing = tk.Label(self, text="Label for testing in member view")
    self.lbl_testing.pack()
