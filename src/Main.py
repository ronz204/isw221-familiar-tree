import tkinter as tk
from tkinter import ttk
from Scheduler import Scheduler
from Events.Broker import Broker

from Screens.PersonScreen import PersonScreen
from Screens.CoupleScreen import CoupleScreen
from Screens.RelatePeopleScreen import RelatePeopleScreen
from Screens.RecentBirthsScreen import RecentBirthsScreen
from Screens.BetweenPeopleScreen import BetweenPeopleScreen
from Screens.DeceasedPeopleScreen import DeceasedPeopleScreen
from Screens.ChildrenTogetherScreen import ChildrenTogetherScreen
from Screens.FirstGradeCousinsScreen import FirstGradeCousinsScreen

from Handlers.Person.BirthPerson.BirthPersonHandler import BirthPersonHandler
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

notebook.add(PersonScreen(notebook, broker), text="Persona")
notebook.add(CoupleScreen(notebook, broker), text="Parejas")
notebook.add(RelatePeopleScreen(notebook, broker), text="Relaciones")

notebook.add(BetweenPeopleScreen(notebook, broker), text="Consulta #1")
notebook.add(FirstGradeCousinsScreen(notebook, broker), text="Consulta #2")
notebook.add(RecentBirthsScreen(notebook, broker), text="Consulta #5")
notebook.add(ChildrenTogetherScreen(notebook, broker), text="Consulta #6")
notebook.add(DeceasedPeopleScreen(notebook, broker), text="Consulta #7")

""" scheduler.start(BirthPersonHandler(broker), 35, "birth")
scheduler.start(DeathPersonHandler(broker), 40, "death")
scheduler.start(BirthdaysPersonHandler(broker), 15, "birthdays") """

def on_closing():
  scheduler.stop_all()
  window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
