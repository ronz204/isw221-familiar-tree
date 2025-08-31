import tkinter as tk
from Domain.Enums.Status import Status
from Domain.Models.Person import Person

class Node:
  def __init__(self, canvas: tk.Canvas, person: Person):
    self.canvas: tk.Canvas = canvas
    self.person: Person = person

    self.rect_id = None
    self.text_id = None

    self.x = 0
    self.y = 0

  def draw(self):
    color = "#ADD8E6" if self.person.gender == "M" else "#FFB6C1"
    if self.person.status == Status.DEATHED.value:
      color = "#D3D3D3"
    
    self.rect_id = self.canvas.create_rectangle(
      fill=color, outline="black", width=2
    )

    self.text_id = self.canvas.create_text(
      text=f"{self.person.name}\n{self.person.age}",
      font=("Arial", 8)
    )
