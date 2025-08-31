import tkinter as tk
from tkinter import ttk

class Node:
    def __init__(self, canvas, person, x, y, width=100, height=60):
        self.canvas = canvas
        self.person = person
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect_id = None
        self.text_id = None
        self.create_node()
    
    def create_node(self):
        # Color basado en género
        color = "#ADD8E6" if self.person.gender == "M" else "#FFB6C1"
        if self.person.status == "D":  # Deceased
            color = "#D3D3D3"
        
        # Crear rectángulo
        self.rect_id = self.canvas.create_rectangle(
            self.x - self.width//2, 
            self.y - self.height//2,
            self.x + self.width//2, 
            self.y + self.height//2,
            fill=color, 
            outline="black", 
            width=2
        )
        
        # Crear texto
        display_text = f"{self.person.name}\n{self.person.age} años"
        self.text_id = self.canvas.create_text(
            self.x, 
            self.y, 
            text=display_text,
            font=("Arial", 8),
            width=self.width-10
        )
    
    def get_position(self):
        return (self.x, self.y)
    
    def move_to(self, new_x, new_y):
        dx = new_x - self.x
        dy = new_y - self.y
        self.canvas.move(self.rect_id, dx, dy)
        self.canvas.move(self.text_id, dx, dy)
        self.x = new_x
        self.y = new_y