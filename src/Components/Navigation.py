import tkinter as tk
from Enums.Colors import Colors
from Components.TabNav import TabNav

class Navigation(tk.Frame):
  def __init__(self, widget: tk.Widget):
    super().__init__(widget, **STYLES)

    tab1 = TabNav(self, text="Crear Familia")
    tab1.pack(fill="x", padx=0, pady=(12, 0))

    tab2 = TabNav(self, text="Crear Miembros")
    tab2.pack(fill="x", padx=0, pady=(8, 0))

    tab3 = TabNav(self, text="Crear Relaciones")
    tab3.pack(fill="x", padx=0, pady=(8, 0))

STYLES = {
  "bg": Colors.GREEN_200.value,
}