import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Searches.ChildrenTogether.ChildrenTogetherBuilder import ChildrenTogetherBuilder
from Application.Handlers.Searchers.ChildrenTogether.ChildrenTogetherHandler import ChildrenTogetherHandler

from Application.Events.Person.ChildrenTogetherFoundEvent import ChildrenTogetherFoundEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class ChildrenTogetherScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = ChildrenTogetherBuilder(self)
    self.children_together_handler = ChildrenTogetherHandler(self.broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(ChildrenTogetherFoundEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)

    self.bus.add(ChildrenTogetherFoundEvent.name, self.on_children_together_found)
    self.bus.add(RegisteredPersonEvent.name, self.on_register_person)

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_search_button(self.on_search_couples)
    self.builder.build_result_section()
    self.builder.build_info_label()

  def on_search_couples(self):
    self.children_together_handler.handle({})

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_children_together_found(self, data: Dict[str, Any]):
    couples = data.get("couples", [])
    self.builder.display_results(couples)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.clear_results()
