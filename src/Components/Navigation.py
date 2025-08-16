import tkinter as tk
from Enums.Pallete import Pallete
from Components.Button import Button

class Navigation(tk.Frame):
  def __init__(self, widget: tk.Widget):
    super().__init__(widget, **STYLES)

    btn_test1 = Button(self, text="Crear Familia")
    btn_test1.grid(row=0, column=0, sticky="ew", padx=0, pady=(12, 0))

    btn_test2 = Button(self, text="Crear Miembros")
    btn_test2.grid(row=1, column=0, sticky="ew", padx=0, pady=(8, 0))

    btn_test3 = Button(self, text="Crear Relaciones")
    btn_test3.grid(row=2, column=0, sticky="ew", padx=0, pady=(8, 0))

    self.grid_columnconfigure(0, weight=1)

STYLES = {
  "bg": Pallete.GREEN_200.value,
}