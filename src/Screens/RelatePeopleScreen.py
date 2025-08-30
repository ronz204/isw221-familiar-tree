import tkinter as tk
from typing import Dict, Any
from Events.Event import Event
from Events.Broker import Broker
from Events.Listener import Listener

from Builders.RelatePeopleScreenBuilder import RelatePeopleScreenBuilder
from Handlers.Person.RelatePeople.RelatePeopleEvent import RelatePeopleEvent
from Handlers.Person.RelatePeople.RelatePeopleHandler import RelatePeopleHandler
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent

class RelatePeopleScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker = broker

    self.builder = RelatePeopleScreenBuilder(self)
    self.relate_people_handler = RelatePeopleHandler(broker)

    self.subscribe_to_events()
    self.setup_ui_components()

  def setup_ui_components(self):
    self.builder.build_layout()
    self.builder.build_container()
    self.builder.build_title()
    self.builder.build_frames()

    self.builder.build_person_field()
    self.builder.build_father_field()
    self.builder.build_mother_field()
    self.builder.build_guardian_field()

    self.builder.build_relate_button(self.on_relate_people)
    self.builder.build_clear_button(self.on_clear_form)
    self.builder.load_data_hydration()

  def subscribe_to_events(self):
    self.broker.subscribe(RelatePeopleEvent.name, self)
    self.broker.subscribe(RegisterPersonEvent.name, self)

  def on_relate_people_success(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
    self.builder.clear_form()

  def on_register_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()

  def handle(self, event: Event):
    if event.name == RelatePeopleEvent.name:
      self.on_relate_people_success(event.data)
    elif event.name == RegisterPersonEvent.name:
      self.on_register_person(event.data)

  def on_relate_people(self):
    data = self.builder.get_form_data()    
    self.relate_people_handler.execute(data)

  def on_clear_form(self):
    self.builder.clear_form()
