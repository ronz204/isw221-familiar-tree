import tkinter as tk

class BaseView(tk.Frame):
  def __init__(self, parent: tk.Widget):
    super().__init__(parent)

  def setup(self) -> None:
    raise NotImplementedError("Subclasses should implement this method")
