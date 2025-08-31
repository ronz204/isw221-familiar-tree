import tkinter as tk
from Presentation.Components.Node import Node

class Edge:
  def __init__(self, canvas: tk.Canvas, start: Node, end: Node):
    self.canvas = canvas
    self.start = start
    self.end = end

    self.line_id = None
