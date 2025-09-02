import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Relate.RelateBuilder import RelateBuilder
from Application.Handlers.RelatePeople.RelatePeopleHandler import RelatePeopleHandler

from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.RelatedPeopleEvent import RelatedPeopleEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class RelateScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = RelateBuilder(self)
    self.relate_people_handler = RelatePeopleHandler(broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(PersonBornEvent.name, self)
    self.broker.subscribe(RelatedPeopleEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)

    self.bus.add(PersonBornEvent.name, self.on_person_born)
    self.bus.add(RelatedPeopleEvent.name, self.on_related_people)
    self.bus.add(RegisteredPersonEvent.name, self.on_registered_person)

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_container()
    self.builder.build_frames()
    self.builder.build_title()

    self.builder.build_person_field()
    self.builder.build_father_field()
    self.builder.build_mother_field()
    self.builder.build_guardian_field()

    self.builder.build_relate_button(self.relate_command)
    self.builder.build_clear_button(self.clear_command)

    self.builder.load_data_hydration()

  def relate_command(self):
    data = self.builder.get_form_data()
    self.relate_people_handler.handle(data)

  def clear_command(self):
    self.builder.clear_form_fields()

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_related_people(self, data: Dict[str, Any]):
    self.builder.clear_form_fields()
  
  def on_person_born(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()

  def on_registered_person(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
