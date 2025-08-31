import tkinter as tk

class Edge:
    def __init__(self, canvas, node1, node2, edge_type="parent_child"):
        self.canvas = canvas
        self.node1 = node1
        self.node2 = node2
        self.edge_type = edge_type  # "parent_child", "couple"
        self.line_id = None
        self.create_edge()
    
    def create_edge(self):
        x1, y1 = self.node1.get_position()
        x2, y2 = self.node2.get_position()
        
        # Color y estilo basado en tipo de relación
        if self.edge_type == "couple":
            color = "red"
            width = 3
        else:  # parent_child
            color = "black"
            width = 2
        
        self.line_id = self.canvas.create_line(
            x1, y1, x2, y2,
            fill=color,
            width=width
        )
    
    def update_position(self):
        if self.line_id:
            x1, y1 = self.node1.get_position()
            x2, y2 = self.node2.get_position()
            self.canvas.coords(self.line_id, x1, y1, x2, y2)