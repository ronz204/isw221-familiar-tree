import tkinter as tk

from Screens.Person.PersonBuilder import PersonBuilder

class PersonScreen(tk.Frame):
  def __init__(self, parent: tk.Widget):
    super().__init__(parent)

    self.builder = PersonBuilder(self)
