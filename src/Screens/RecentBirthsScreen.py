import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener

from Builders.RecentBirthsScreenBuilder import RecentBirthsScreenBuilder
from Handlers.Queries.RecentBirths.RecentBirthsEvent import RecentBirthsEvent
from Handlers.Queries.RecentBirths.RecentBirthsHandler import RecentBirthsHandler
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent

class RecentBirthsScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = RecentBirthsScreenBuilder(self)
    self.recent_births_handler = RecentBirthsHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()
    
    self.builder.build_search_button(self.on_search_recent_births)
    self.builder.build_result_area()
    self.builder.build_info_label()

  def subscribe_to_events(self):
    self.broker.subscribe(RecentBirthsEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_recent_births_result(self, data: Dict[str, Any]):
    births_list = data.get("births", [])
    self.builder.populate_results(births_list)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.clear_results()

  def handle(self, event: Event):
    if event.name == RecentBirthsEvent.name:
      self.on_recent_births_result(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_search_recent_births(self):
    self.recent_births_handler.execute({})
