import tkinter as tk
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

    self.form = tk.Frame(self, bd=2, relief=tk.GROOVE, bg="#f0f0f0")
    self.form.config(padx=30, pady=25)
    self.form.grid(row=1, column=1)

    self.lbl_title = Label(self.form, text="Datos de la Familia")
    self.lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    self.lbl_name = Label(self.form, text="Nombre")
    self.lbl_name.grid(row=1, column=0, padx=(0, 10), pady=8)

    self.entry_name = Field(self.form, width=25)
    self.entry_name.grid(row=1, column=1, padx=(0, 0), pady=8)

    self.btn_save = Button(self.form, text="Save")
    self.btn_save.grid(row=2, column=0, columnspan=2, pady=(20, 0))
