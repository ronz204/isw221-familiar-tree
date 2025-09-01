import tkinter as tk
from Domain.Models.Person import Person

class Node:
  def __init__(self, canvas: tk.Canvas, person: Person, x: int = 0, y: int = 0):
    self.canvas = canvas
    self.person = person

    self.x = x
    self.y = y

    self.width = 120
    self.height = 60

    self.rect_id = None
    self.text_id = None

  def get_node_color(self):
    if self.person.status == "D": return "#D3D3D3"
    return "#ADD8E6" if self.person.gender == "M" else "#FFB6C1"
  
  def get_center(self):
    return (self.x + self.width // 2, self.y + self.height // 2)
  
  def get_connection_points(self):
    center_x, center_y = self.get_center()
    return {
      "top": (center_x, self.y),
      "bottom": (center_x, self.y + self.height),
      "left": (self.x, center_y),
      "right": (self.x + self.width, center_y)
    }

  def move_to(self, new_x: int, new_y: int):
    if self.rect_id and self.text_id:
      delta_x, delta_y = new_x - self.x, new_y - self.y
      self.canvas.move(self.rect_id, delta_x, delta_y)
      self.canvas.move(self.text_id, delta_x, delta_y)
      self.x, self.y = new_x, new_y

  def draw(self):
    self.rect_id = self.canvas.create_rectangle(
      self.x, self.y, self.x + self.width, self.y + self.height,
      fill=self.get_node_color(), outline="black", width=2)

    center_x, center_y = self.get_center()
    
    self.text_id = self.canvas.create_text(
      center_x, center_y,
      text=f"{self.person.name}\n{self.person.age} años",
      font=("Arial", 9), anchor="center")
