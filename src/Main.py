import tkinter as tk
from tkinter import ttk
from Application.Events.Broker import Broker

from Presentation.Screens.Match.MatchScreen import MatchScreen
from Presentation.Screens.Person.PersonScreen import PersonScreen
from Presentation.Screens.Relate.RelateScreen import RelateScreen
from Presentation.Screens.Family.FamilyScreen import FamilyScreen
from Presentation.Screens.Timeline.TimelineScreen import TimelineScreen

from Presentation.Screens.Searches.ChildrenTogether.ChildrenTogetherScreen import ChildrenTogetherScreen
from Presentation.Screens.Searches.BetweenTwoPeople.BetweenTwoPeopleScreen import BetweenTwoPeopleScreen

window = tk.Tk()
broker = Broker()

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

window.mainloop()
