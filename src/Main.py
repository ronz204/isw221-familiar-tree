import tkinter as tk
from tkinter import ttk
from Events.Broker import Broker
from Screens.FamilyScreen import FamilyScreen
from Screens.PersonScreen import PersonScreen
from Screens.RelateScreen import RelateScreen

from Helpers.ScheduleHelper import ScheduleHelper
from Handlers.Person.Birthdate.BirthdateHandler import BirthdateHandler
from Handlers.Person.Deathdate.DeathdateHandler import DeathdateHandler

window = tk.Tk()
broker = Broker()
scheduler = ScheduleHelper()

window.geometry("1200x600")
window.title("Familiar Tree")
window.resizable(False, False)
window.config(padx=20, pady=20)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

notebook.add(FamilyScreen(notebook, broker), text="Familia")
notebook.add(PersonScreen(notebook, broker), text="Persona")
notebook.add(RelateScreen(notebook, broker), text="Relaciones")

scheduler.start(BirthdateHandler(broker), 10, "birthdate")
# scheduler.start(DeathdateHandler(broker), 15, "deathdate")

def on_closing():
  scheduler.stop_all()
  window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
