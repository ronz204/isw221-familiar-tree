import tkinter as tk
from Enums.Colors import Colors
from Components.Label import Label
from Components.Field import Field
from Views.BaseView import BaseView
from Components.Button import Button

class FamilyView(BaseView):
  def __init__(self, widget: tk.Widget):
    super().__init__(widget)
    self.render()

  def render(self) -> None:
    for index in range(3):
      self.grid_rowconfigure(index, weight=1)
      self.grid_columnconfigure(index, weight=1)

    self.form = tk.Frame(self, bg=Colors.BACKGROUND.value, padx=40, pady=35)
    self.form.grid(row=1, column=1, sticky="nsew")


    self.lbl_title = Label(self.form, text="Registro de Familias")
    self.lbl_title.config(font=("Arial", 16, "bold"))
    self.lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 30), sticky="w")

    self.lbl_name = Label(self.form, text="Nombre de la familia:")
    self.lbl_name.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 8))

    self.entry_name = Field(self.form, width=30)
    self.entry_name.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 20))


    button_frame = tk.Frame(self.form, bg="#ffffff")
    button_frame.grid(row=3, column=0, columnspan=2, pady=(20, 0))

    self.btn_cancel = Button(button_frame, text="Discard")
    self.btn_cancel.pack(side=tk.LEFT, padx=(0, 10))

    self.btn_save = Button(button_frame, text="Save")
    self.btn_save.pack(side=tk.LEFT)

    self.form.grid_columnconfigure(0, weight=1)
