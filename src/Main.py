""" from Database.Peewee import db
from Database.Migrator import Migrator

migrator = Migrator(db)
migrator.migrate() """

import tkinter as tk

window = tk.Tk()

window.geometry("1200x600")
window.title("Familiar Tree")
window.resizable(False, False)

window.mainloop()
