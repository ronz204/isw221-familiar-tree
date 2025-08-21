import tkinter as tk
from Enums.Colors import Colors
from Routing.Router import Router
from Routing.Routes import Routes
from Components.Linker import Linker

class Layout(tk.Frame):
  def __init__(self, widget: tk.Widget):
    super().__init__(widget, **STYLES)

    self.grid_rowconfigure(0, weight=1)

    self.grid_columnconfigure(0, weight=1)
    self.grid_columnconfigure(1, weight=19)

    self.left_frame = tk.Frame(self, bg=Colors.GREEN_900.value)
    self.left_frame.grid(row=0, column=0, sticky="nsew")

    self.right_frame = tk.Frame(self, bg=Colors.WHITE_100.value, padx=32, pady=28)
    self.right_frame.grid(row=0, column=1, sticky="nsew")

    self.router = Router(self.right_frame)
    self.render_linkers()
    self.router.navigate(Routes.FAMILY.value)

  def render_linkers(self):
    self.linker1 = Linker(self.left_frame, text="Registrar Familia")
    self.linker1.config(command=lambda: self.router.navigate(Routes.FAMILY.value))
    self.linker1.pack(fill="x", padx=0, pady=(12, 0))

    self.linker2 = Linker(self.left_frame, text="Registrar Miembro")
    self.linker2.config(command=lambda: self.router.navigate(Routes.MEMBER.value))
    self.linker2.pack(fill="x", padx=0, pady=(8, 0))

    self.linker3 = Linker(self.left_frame, text="Registrar Relacion")
    self.linker3.config(command=lambda: self.router.navigate(Routes.RELATION.value))
    self.linker3.pack(fill="x", padx=0, pady=(8, 0))

STYLES = {
  "bg": Colors.GREEN_200.value,
}
