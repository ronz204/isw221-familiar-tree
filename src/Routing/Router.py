import tkinter as tk
from Views.BaseView import BaseView
from typing import Type, Dict, Optional

class Router:
  def __init__(self, widget: tk.Widget):
    self.widget: tk.Widget = widget
    self.current: Optional[BaseView] = None
    self.views: Dict[Type[BaseView], BaseView] = {}

  def navigate(self, view: Type[BaseView]) -> None:
    if self.current: self.current.grid_forget()

    if view not in self.views:
      self.views[view] = view(self.widget)

    self.current = self.views[view]
    self.current.grid(row=0, column=0, sticky="nsew")
