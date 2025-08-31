import tkinter as tk
from Domain.Models.Person import Person

class Node:
  def __init__(self, canvas: tk.Canvas, person: Person):
    self.canvas: tk.Canvas = canvas
    self.person: Person = person

    self.rect_id = None
    self.text_id = None

    self.x = 0
    self.y = 0
