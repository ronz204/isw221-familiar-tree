""" from Database.Peewee import db
from Database.Migrator import Migrator

migrator = Migrator(db)
migrator.migrate() """

import tkinter as tk
from Components.Layout import Layout

window = tk.Tk()

window.geometry("1200x600")
window.title("Familiar Tree")

layout = Layout(window)
layout.pack(fill=tk.BOTH, expand=True)

window.resizable(False, False)

window.mainloop()
