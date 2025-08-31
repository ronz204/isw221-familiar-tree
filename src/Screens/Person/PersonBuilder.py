import tkinter as tk
from tkinter import ttk
from typing import Any, Callable, List

class PersonBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent: tk.Widget = parent
