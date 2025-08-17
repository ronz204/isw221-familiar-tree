import tkinter as tk
from Enums.Pallete import Pallete
from Components.TabNav import TabNav

class Navigation(tk.Frame):
  def __init__(self, widget: tk.Widget):
    super().__init__(widget, **STYLES)

    tab1 = TabNav(self, text="Crear Familia")
    tab1.grid(row=0, column=0, sticky="ew", padx=0, pady=(12, 0))

    tab2 = TabNav(self, text="Crear Miembros")
    tab2.grid(row=1, column=0, sticky="ew", padx=0, pady=(8, 0))

    tab3 = TabNav(self, text="Crear Relaciones")
    tab3.grid(row=2, column=0, sticky="ew", padx=0, pady=(8, 0))

    self.grid_columnconfigure(0, weight=1)

STYLES = {
  "bg": Pallete.GREEN_200.value,
}