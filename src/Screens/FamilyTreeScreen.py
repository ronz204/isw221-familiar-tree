import tkinter as tk
from tkinter import ttk
from Models.Person import Person
from Models.Relation import Relation
from Components.Node import Node
from Components.Edge import Edge

class FamilyTreeScreen(tk.Frame):
    # Configuración de nodos como constante de clase
    NODE_CONFIG = {
        'width': 120, 'height': 80, 'level_height': 150,
        'horizontal_spacing': 50, 'start_y': 100, 'min_start_x': 200
    }
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.nodes = {}
        self.edges = []
        self.levels = {}
        self._setup_ui()
        self._load_data()
    
    def _setup_ui(self):
        """Configura toda la interfaz"""
        # Título
        tk.Label(self, text="Árbol Genealógico", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Canvas con scrollbars
        canvas_frame = tk.Frame(self)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.canvas = tk.Canvas(canvas_frame, bg="white")
        v_scroll = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        h_scroll = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        
        self.canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        # Grid layout
        self.canvas.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")
        canvas_frame.grid_rowconfigure(0, weight=1)
        canvas_frame.grid_columnconfigure(0, weight=1)
        
        # Botón volver
        ttk.Button(self, text="Volver", command=self.go_back).pack(pady=10)
    
    def _load_data(self):
        """Carga y renderiza el árbol"""
        people = list(Person.select())
        
        if not people:
            self.canvas.create_text(400, 300, text="No hay personas en la base de datos", 
                                   font=("Arial", 14), fill="gray")
            return
        
        self._organize_levels(people)
        self._create_nodes()
        self._create_edges()
        self._update_scroll()
    
    def _organize_levels(self, people):
        """Organiza personas por generaciones de forma optimizada"""
        visited = set()
        people_dict = {p.id: p for p in people}
        
        # Nivel 0: ancestros
        self.levels[0] = [p for p in people if not p.father_id and not p.mother_id]
        visited.update(p.id for p in self.levels[0])
        
        level = 0
        while len(visited) < len(people):
            children = set()
            
            # Buscar hijos del nivel actual
            if level in self.levels:
                for parent in self.levels[level]:
                    children.update(p.id for p in people 
                                  if (p.father_id == parent.id or p.mother_id == parent.id) 
                                  and p.id not in visited)
            
            # Si no hay hijos, agregar personas restantes
            if not children:
                children = {p.id for p in people if p.id not in visited}
            
            if children:
                level += 1
                self.levels[level] = [people_dict[pid] for pid in children]
                visited.update(children)
            else:
                break
    
    def _create_nodes(self):
        """Crea todos los nodos optimizadamente"""
        for level, people in self.levels.items():
            y_pos = self.NODE_CONFIG['start_y'] + level * self.NODE_CONFIG['level_height']
            
            # Calcular posiciones X
            total_width = len(people) * (self.NODE_CONFIG['width'] + self.NODE_CONFIG['horizontal_spacing'])
            start_x = max(self.NODE_CONFIG['min_start_x'], (1000 - total_width) // 2)
            
            # Crear nodos
            for i, person in enumerate(people):
                x_pos = start_x + i * (self.NODE_CONFIG['width'] + self.NODE_CONFIG['horizontal_spacing'])
                self.nodes[person.id] = Node(self.canvas, person, x_pos, y_pos, 
                                           self.NODE_CONFIG['width'], self.NODE_CONFIG['height'])
    
    def _create_edges(self):
        """Crea todas las aristas optimizadamente"""
        # Aristas padre-hijo
        for person_id, node in self.nodes.items():
            person = node.person
            
            for parent_id in [person.father_id, person.mother_id]:
                if parent_id and parent_id in self.nodes:
                    self.edges.append(Edge(self.canvas, self.nodes[parent_id], node, "parent_child"))
        
        # Aristas de parejas
        for relation in Relation.select():
            if relation.man_id in self.nodes and relation.woman_id in self.nodes:
                self.edges.append(Edge(self.canvas, self.nodes[relation.man_id], 
                                     self.nodes[relation.woman_id], "couple"))
    
    def _update_scroll(self):
        """Actualiza la región de scroll"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def go_back(self):
        """Regresa al menú principal"""
        self.parent.show_main_menu()