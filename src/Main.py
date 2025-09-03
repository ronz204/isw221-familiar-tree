import tkinter as tk
from tkinter import ttk
from Application.Events.Broker import Broker

from Application.Triggers.BirthTrigger import BirthTrigger
from Application.Triggers.DeathTrigger import DeathTrigger
from Application.Triggers.BirthdayTrigger import BirthdayTrigger
from Application.Service.SchedulerService import SchedulerService

from Presentation.Screens.Match.MatchScreen import MatchScreen
from Presentation.Screens.Person.PersonScreen import PersonScreen
from Presentation.Screens.Relate.RelateScreen import RelateScreen
from Presentation.Screens.Family.FamilyScreen import FamilyScreen
from Presentation.Screens.Timeline.TimelineScreen import TimelineScreen

from Presentation.Screens.Searches.RecentBirths.RecentBirthsScreen import RecentBirthsScreen
from Presentation.Screens.Searches.DeathedPeople.DeathedPeopleScreen import DeathedPeopleScreen
from Presentation.Screens.Searches.ChildrenTogether.ChildrenTogetherScreen import ChildrenTogetherScreen
from Presentation.Screens.Searches.BetweenTwoPeople.BetweenTwoPeopleScreen import BetweenTwoPeopleScreen
from Presentation.Screens.Searches.MaternalAncestors.MaternalAncestorsScreen import MaternalAncestorsScreen
from Presentation.Screens.Searches.LivingDescendants.LivingDescendantsScreen import LivingDescendantsScreen
from Presentation.Screens.Searches.FirstGradeCousins.FirstGradeCousinsScreen import FirstGradeCousinsScreen

window = tk.Tk()
broker = Broker()

scheduler = SchedulerService()

window.geometry("1200x600")
window.title("Familiar Tree")
window.resizable(False, False)
window.config(padx=20, pady=20)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

notebook.add(PersonScreen(notebook, broker), text="Registrar Personas")
notebook.add(RelateScreen(notebook, broker), text="Relacionar Personas")
notebook.add(MatchScreen(notebook, broker), text="Emparejar Personas")
notebook.add(FamilyScreen(notebook, broker), text="Árbol Genealógico")
notebook.add(TimelineScreen(notebook, broker), text="Línea de Tiempo")

notebook.add(BetweenTwoPeopleScreen(notebook, broker), text="Busqueda #1")
notebook.add(ChildrenTogetherScreen(notebook, broker), text="Busqueda #2")
notebook.add(DeathedPeopleScreen(notebook, broker), text="Busqueda #3")
notebook.add(FirstGradeCousinsScreen(notebook, broker), text="Busqueda #4")
notebook.add(LivingDescendantsScreen(notebook, broker), text="Busqueda #5")
notebook.add(MaternalAncestorsScreen(notebook, broker), text="Busqueda #6")
notebook.add(RecentBirthsScreen(notebook, broker), text="Busqueda #7")

""" scheduler.start(BirthTrigger(broker), "birth", 10)
scheduler.start(DeathTrigger(broker), "death", 20)
scheduler.start(BirthdayTrigger(broker), "birthday", 5) """

def on_closing():
  scheduler.stop_all()
  window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
