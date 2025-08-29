import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener

from Builders.ChildrenTogetherScreenBuilder import ChildrenTogetherScreenBuilder
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent
from Handlers.Queries.ChildrenTogether.ChildrenTogetherEvent import ChildrenTogetherEvent
from Handlers.Queries.ChildrenTogether.ChildrenTogetherHandler import ChildrenTogetherHandler

class ChildrenTogetherScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = ChildrenTogetherScreenBuilder(self)
    self.children_together_handler = ChildrenTogetherHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()
    
    self.builder.build_search_button(self.on_search_couples)
    self.builder.build_result_area()
    self.builder.build_info_label()

  def subscribe_to_events(self):
    self.broker.subscribe(ChildrenTogetherEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_children_together_result(self, data: Dict[str, Any]):
    couples_list = data.get("couples", [])
    self.builder.populate_results(couples_list)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.clear_results()

  def handle(self, event: Event):
    if event.name == ChildrenTogetherEvent.name:
      self.on_children_together_result(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_search_couples(self):
    self.children_together_handler.execute({})
