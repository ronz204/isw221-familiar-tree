import tkinter as tk
from tkinter import ttk
from Events.Broker import Broker
from Screens.FamilyScreen import FamilyScreen
from Screens.PersonScreen import PersonScreen

window = tk.Tk()
broker = Broker()

window.geometry("1200x600")
window.title("Familiar Tree")
window.resizable(False, False)
window.config(padx=20, pady=20)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

notebook.add(FamilyScreen(notebook, broker), text="Familia")
notebook.add(PersonScreen(notebook, broker), text="Persona")

window.mainloop()
