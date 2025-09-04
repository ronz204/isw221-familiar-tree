import tkinter as tk
from Presentation.Components.Node import Node

class Edge:
  def __init__(self, canvas: tk.Canvas, start: Node, end: Node, type: str = "child"):
    self.canvas = canvas

    self.start: Node = start
    self.end: Node = end

    self.type: str = type
    self.line_id: int = None

  def draw(self):
    start_points = self.start.get_connection_points()
    end_points = self.end.get_connection_points()
    
    start_point, end_point, color, width = self.get_line_config(start_points, end_points)

    if self.type == "guardian":
      self.line_id = self.canvas.create_line(
        *start_point, *end_point,
        fill=color, width=width, dash=(5, 3))
    else:
      self.line_id = self.canvas.create_line(
        *start_point, *end_point,
        fill=color, width=width)

  def update_position(self):
    if self.line_id:
      self.canvas.delete(self.line_id)
      self.draw()

  def get_line_config(self, start_points, end_points):
    if self.type == "spouse":
      direction = "right" if self.start.x < self.end.x else "left"
      opposite = "left" if direction == "right" else "right"
      return start_points[direction], end_points[opposite], "red", 3
    elif self.type == "guardian":
      direction = "bottom" if self.start.y < self.end.y else "top"
      opposite = "top" if direction == "bottom" else "bottom"
      return start_points[direction], end_points[opposite], "green", 2
    else:
      direction = "bottom" if self.start.y < self.end.y else "top"
      opposite = "top" if direction == "bottom" else "bottom"
      return start_points[direction], end_points[opposite], "blue", 2
