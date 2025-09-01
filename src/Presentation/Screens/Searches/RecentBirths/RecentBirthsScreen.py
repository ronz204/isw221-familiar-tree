import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Searches.RecentBirths.RecentBirthsBuilder import RecentBirthsBuilder
from Application.Handlers.Searchers.RecentBirths.RecentBirthsHandler import RecentBirthsHandler

from Application.Events.Person.RecentBirthsFoundEvent import RecentBirthsFoundEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class RecentBirthsScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = RecentBirthsBuilder(self)
    self.recent_births_handler = RecentBirthsHandler(self.broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(RecentBirthsFoundEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)

    self.bus.add(RecentBirthsFoundEvent.name, self.on_recent_births_found)
    self.bus.add(RegisteredPersonEvent.name, self.on_registered_person)

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()
    self.builder.build_search_button(self.on_search_command)
    self.builder.build_result_section()
    self.builder.build_info_label()
    self.builder.clear_results()

  def on_search_command(self):
    self.recent_births_handler.handle({})

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_recent_births_found(self, data: Dict[str, Any]):
    births = data.get("births", [])
    self.builder.display_results(births)

  def on_registered_person(self, data: Dict[str, Any]):
    self.builder.clear_results()
