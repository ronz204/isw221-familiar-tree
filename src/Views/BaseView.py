import tkinter as tk
from Events.EventBroker import EventBroker

class BaseView(tk.Frame):
  def __init__(self, parent: tk.Widget, broker: EventBroker):
    super().__init__(parent)
    self.broker = broker

  def render(self) -> None:
    raise NotImplementedError("Subclasses should implement this method")
