import tkinter as tk
from tkinter import ttk
from Application.Events.Broker import Broker
from Presentation.Screens.Person.PersonScreen import PersonScreen
from Presentation.Screens.Relate.RelateScreen import RelateScreen

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

window.mainloop()
