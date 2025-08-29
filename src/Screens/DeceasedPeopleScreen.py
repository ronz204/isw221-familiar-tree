import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener

from Builders.DeceasedPeopleScreenBuilder import DeceasedPeopleScreenBuilder
from Handlers.Queries.DeceasedPeople.DeceasedPeopleHandler import DeceasedPeopleHandler
from Handlers.Queries.DeceasedPeople.DeceasedPeopleEvent import DeceasedPeopleEvent
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent

class DeceasedPeopleScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = DeceasedPeopleScreenBuilder(self)
    self.deceased_people_handler = DeceasedPeopleHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()
    
    self.builder.build_search_button(self.on_search_deceased)
    self.builder.build_result_area()
    self.builder.build_info_label()

  def subscribe_to_events(self):
    self.broker.subscribe(DeceasedPeopleEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_deceased_people_result(self, data: Dict[str, Any]):
    deceased_list = data.get("deceased", [])
    self.builder.populate_results(deceased_list)

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.clear_results()

  def handle(self, event: Event):
    if event.name == DeceasedPeopleEvent.name:
      self.on_deceased_people_result(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_search_deceased(self):
    self.deceased_people_handler.execute({})