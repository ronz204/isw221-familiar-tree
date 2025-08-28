import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener

from Builders.RelateScreenBuilder import RelateScreenBuilder
from Handlers.Person.RelatePerson.RelatePersonEvent import RelatePersonEvent
from Handlers.Person.RelatePerson.RelatePersonHandler import RelatePersonHandler
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent

class RelateScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = RelateScreenBuilder(self)
    self.relate_person_handler = RelatePersonHandler(self.broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_man_field()
    self.builder.build_woman_field()
    self.builder.build_year_field()

    self.builder.build_relate_button(self.on_save_relation)
    self.builder.build_discard_button(self.on_discard_relation)
    self.builder.load_data_hydration()

  def subscribe_to_events(self):
    self.broker.subscribe(RelatePersonEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_relate_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
    self.builder.clear_form()

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()

  def handle(self, event: Event):
    if event.name == RelatePersonEvent.name:
      self.on_relate_person(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_save_relation(self):
    data = self.builder.get_form_data()
    self.relate_person_handler.execute(data)

  def on_discard_relation(self):
    self.builder.clear_form()
