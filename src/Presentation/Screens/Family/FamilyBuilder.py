import tkinter as tk
from tkinter import ttk
from typing import List, Dict
from Domain.Models.Person import Person
from Domain.Models.Relation import Relation
from Presentation.Components.Node import Node
from Presentation.Components.Edge import Edge

class FamilyBuilder:
  def __init__(self, parent: tk.Widget):
    self.parent: tk.Widget = parent
    self.canvas: tk.Canvas = None

    self.edges: List[Edge] = []
    self.people: List[Person] = []
    self.nodes: Dict[int, Node] = {}

  def setup_grid(self):
    self.parent.grid_rowconfigure(0, weight=1)
    self.parent.grid_columnconfigure(0, weight=1)

  def build_title(self):
    self.title = tk.Label(self.parent, text="Árbol Genealógico", font=("Arial", 16, "bold"))
    self.title.pack(pady=10)

  def build_canvas(self):
    self.canvas_frame = tk.Frame(self.parent)
    self.canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

  def build_scrollers(self):
    self.canvas = tk.Canvas(self.canvas_frame, bg="white")
    self.v_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
    self.h_scroll = ttk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)

    self.canvas.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

    self.canvas.grid(row=0, column=0, sticky="nsew")
    self.v_scroll.grid(row=0, column=1, sticky="ns")
    self.h_scroll.grid(row=1, column=0, sticky="ew")
    self.canvas_frame.grid_rowconfigure(0, weight=1)
    self.canvas_frame.grid_columnconfigure(0, weight=1)

  def build_legend_info(self):
    legend_frame = tk.Frame(self.parent)
    legend_frame.pack(pady=5)
    
    tk.Label(legend_frame, text="Leyenda:", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
    tk.Label(legend_frame, text="Hombres", fg="blue").pack(side=tk.LEFT, padx=5)
    tk.Label(legend_frame, text="Mujeres", fg="red").pack(side=tk.LEFT, padx=5)
    tk.Label(legend_frame, text="Fallecidos", fg="gray").pack(side=tk.LEFT, padx=5)
    tk.Label(legend_frame, text="— Pareja (rojo)", fg="red").pack(side=tk.LEFT, padx=5)
    tk.Label(legend_frame, text="— Padre/Hijo (azul)", fg="blue").pack(side=tk.LEFT, padx=5)
    tk.Label(legend_frame, text="--- Tutor Legal (verde)", fg="green").pack(side=tk.LEFT, padx=5)

  def load_data_hydration(self):
    self.people = list(Person.select())

  def clear_family_tree(self):
    if self.canvas:
      self.canvas.delete("all")
    
    self.edges.clear()
    self.nodes.clear()

  def build_family_tree(self):
    if not self.people: 
      self.clear_family_tree()
      return

    self.clear_family_tree()
    
    self.create_nodes()
    self.calculate_positions()
    self.draw_nodes()
    self.create_edges()
    self.draw_edges()
    self.update_scroll_region()

  def create_nodes(self):
    for person in self.people:
      self.nodes[person.id] = Node(self.canvas, person)

  def calculate_positions(self):
    roots = [p for p in self.people if p.father is None and p.mother is None]
    if not roots:
      roots = sorted(self.people, key=lambda p: p.age, reverse=True)[:2]

    levels = self.organize_by_levels(roots)
    y_spacing, x_spacing = 150, 140
    
    for level_index, level_people in enumerate(levels):
      y = 50 + level_index * y_spacing
      for person_index, person in enumerate(level_people):
        x = 50 + person_index * x_spacing
        self.nodes[person.id].x = x
        self.nodes[person.id].y = y

  def organize_by_levels(self, roots):
    levels = []
    processed = set()
    current_level = roots.copy()
    
    while current_level:
      levels.append(current_level.copy())
      processed.update(p.id for p in current_level)
      
      next_level = []
      for person in current_level:
        children = [p for p in self.people 
                   if (p.father and p.father.id == person.id) or 
                      (p.mother and p.mother.id == person.id)]
        
        for child in children:
          if child.id not in processed and child not in next_level:
            next_level.append(child)
      
      current_level = next_level
    
    remaining = [p for p in self.people if p.id not in processed]
    if remaining:
      levels.append(remaining)
    
    return levels

  def draw_nodes(self):
    for node in self.nodes.values():
      node.draw()

  def create_edges(self):
    self.edges = []

    # Parent-Child Relationships
    for person in self.people:
      if person.father and person.father.id in self.nodes:
        self.edges.append(Edge(self.canvas, self.nodes[person.father.id], 
                              self.nodes[person.id], "child"))
      
      if person.mother and person.mother.id in self.nodes:
        self.edges.append(Edge(self.canvas, self.nodes[person.mother.id], 
                              self.nodes[person.id], "child"))

    # Guardian Relationships
    for person in self.people:
      if person.guard and person.guard.id in self.nodes:
        self.edges.append(Edge(self.canvas, self.nodes[person.guard.id], 
                              self.nodes[person.id], "guardian"))

    # Spousal Relationships
    relations = list(Relation.select().where(Relation.status == "C"))
    for relation in relations:
      if relation.man.id in self.nodes and relation.woman.id in self.nodes:
        self.edges.append(Edge(self.canvas, self.nodes[relation.man.id], 
                              self.nodes[relation.woman.id], "spouse"))

  def draw_edges(self):
    for edge in self.edges:
      edge.draw()

  def update_scroll_region(self):
    self.canvas.update_idletasks()
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))
