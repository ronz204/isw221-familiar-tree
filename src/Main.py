import tkinter as tk
from tkinter import ttk
from Scheduler import Scheduler
from Events.Broker import Broker

from Screens.FamilyScreen import FamilyScreen
from Screens.PersonScreen import PersonScreen
from Screens.RelateScreen import RelateScreen

from Handlers.Person.DeathPerson.DeathPersonHandler import DeathPersonHandler
from Handlers.Person.BirthdaysPerson.BirthdaysPersonHandler import BirthdaysPersonHandler

window = tk.Tk()
broker = Broker()
scheduler = Scheduler()

window.geometry("1200x600")
window.title("Familiar Tree")
window.resizable(False, False)
window.config(padx=20, pady=20)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

notebook.add(FamilyScreen(notebook, broker), text="Familia")
notebook.add(PersonScreen(notebook, broker), text="Persona")
notebook.add(RelateScreen(notebook, broker), text="Relaciones")

scheduler.start(DeathPersonHandler(broker), 40, "death")
scheduler.start(BirthdaysPersonHandler(broker), 15, "birthdays")

def on_closing():
  scheduler.stop_all()
  window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
