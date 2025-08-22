import tkinter as tk
from Views.BaseView import BaseView
from typing import Type, Dict, Optional
from Events.EventBroker import EventBroker

class Router:
  def __init__(self, widget: tk.Widget):
    self.widget: tk.Widget = widget
    self.broker: EventBroker = EventBroker()

    self.current: Optional[BaseView] = None
    self.views: Dict[Type[BaseView], BaseView] = {}

    self.widget.grid_propagate(False)
    self.widget.grid_rowconfigure(0, weight=1)
    self.widget.grid_columnconfigure(0, weight=1)

  def navigate(self, view: Type[BaseView]) -> None:
    if self.current: self.current.grid_forget()

    if view not in self.views:
      self.views[view] = view(self.widget, self.broker)

    self.current = self.views[view]
    self.current.grid(row=0, column=0, sticky="nsew")
