""" from Database.Peewee import db
from Database.Migrator import Migrator

migrator = Migrator(db)
migrator.migrate() """

import tkinter as tk
from Views.DashView import DashView

window = tk.Tk()

window.geometry("1200x600")
window.title("Familiar Tree")

dash_view = DashView(window)
dash_view.pack(fill=tk.BOTH, expand=True)

window.resizable(False, False)

window.mainloop()
