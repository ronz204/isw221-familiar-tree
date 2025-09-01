import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Searches.DeathedPeople.DeathedPeopleBuilder import DeathedPeopleBuilder
from Application.Handlers.Searchers.DeathedPeople.DeathedPeopleHandler import DeathedPeopleHandler

from Application.Events.Person.DeathedPeopleFoundEvent import DeathedPeopleFoundEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class DeathedPeopleScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = DeathedPeopleBuilder(self)
    self.deathed_people_handler = DeathedPeopleHandler(self.broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(DeathedPeopleFoundEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)

    self.bus.add(DeathedPeopleFoundEvent.name, self.on_deathed_people_found)
    self.bus.add(RegisteredPersonEvent.name, self.on_register_person)

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
    self.deathed_people_handler.handle({})

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_deathed_people_found(self, data: Dict[str, Any]):
    deathed_people = data.get("deathed", [])
    self.builder.display_results(deathed_people)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.clear_results()
