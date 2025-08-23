import tkinter as tk
from Events.EventBroker import EventBroker
from Handlers.Family.CreateFamily.CreateFamilyHandler import CreateFamilyHandler

class FamilyScreen(tk.Frame):
  def __init__(self, parent: tk.Widget, broker: EventBroker):
    super().__init__(parent)
    self.handler = CreateFamilyHandler(broker)
    self.broker = broker

    self.setup_layout()
    self.render_widgets()

  def setup_layout(self):
    for index in range(3):
      self.grid_rowconfigure(index, weight=1)
      self.grid_columnconfigure(index, weight=1)

  def render_widgets(self):
    self.container = tk.Frame(self)
    self.container.grid_columnconfigure(0, weight=1)
    self.container.grid(row=1, column=1, padx=40, pady=40)

    self.title = tk.Label(self.container, text="Registrar Familia", font=("", 14, "bold"))
    self.title.grid(row=0, column=0, columnspan=2, pady=(0, 30))

    self.name_label = tk.Label(self.container, text="Nombre de la familia:")
    self.name_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 5))
    self.name_entry = tk.Entry(self.container, font=("", 12), width=40)
    self.name_entry.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 30))


    self.button_frame = tk.Frame(self.container)
    self.button_frame.config(bd=2, padx=15, pady=15)
    self.button_frame.grid_columnconfigure(0, weight=1)
    self.button_frame.grid_columnconfigure(1, weight=1)
    self.button_frame.grid(row=3, column=0, columnspan=2, sticky="ew")

    self.save_button = tk.Button(self.button_frame, text="Guardar", command=self.on_save)
    self.save_button.config(width=15, height=2, font=("", 10, "bold"))
    self.save_button.grid(row=0, column=0, padx=(0, 10), sticky="e")

    self.cancel_button = tk.Button(self.button_frame, text="Cancelar", command=self.on_cancel)
    self.cancel_button.config(width=15, height=2, font=("", 10, "bold"))
    self.cancel_button.grid(row=0, column=1, sticky="w")
  
  def on_save(self):
    self.handler.handle({
      "name": self.name_entry.get()
    })
    self.clear_form()

  def on_cancel(self):
    self.clear_form()

  def clear_form(self):
    self.name_entry.delete(0, tk.END)
