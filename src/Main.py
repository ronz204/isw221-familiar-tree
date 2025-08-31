import tkinter as tk
from tkinter import ttk

from Screens.Person.PersonScreen import PersonScreen

window = tk.Tk()

window.geometry("1200x600")
window.title("Familiar Tree")
window.resizable(False, False)
window.config(padx=20, pady=20)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

notebook.add(PersonScreen(notebook), text="Registrar Personas")

window.mainloop()
