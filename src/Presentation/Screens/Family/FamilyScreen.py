import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Family.FamilyBuilder import FamilyBuilder
from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.DeathedPersonEvent import DeathedPersonEvent
from Application.Events.Person.RelatedPeopleEvent import RelatedPeopleEvent
from Application.Events.Person.MatchedPeopleEvent import MatchedPeopleEvent
from Application.Events.Person.YearsCelebratedEvent import YearsCelebratedEvent

from Application.Handlers.WidowedPerson.WidowedPersonHandler import WidowedPersonHandler

class FamilyScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = FamilyBuilder(self)
    self.widowed_person_handler = WidowedPersonHandler(broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(PersonBornEvent.name, self)
    self.broker.subscribe(DeathedPersonEvent.name, self)
    self.broker.subscribe(RelatedPeopleEvent.name, self)
    self.broker.subscribe(MatchedPeopleEvent.name, self)
    self.broker.subscribe(YearsCelebratedEvent.name, self)

    self.bus.add(PersonBornEvent.name, self.setup_family_tree)
    self.bus.add(DeathedPersonEvent.name, self.on_deathed_person)
    self.bus.add(RelatedPeopleEvent.name, self.setup_family_tree)
    self.bus.add(MatchedPeopleEvent.name, self.setup_family_tree)
    self.bus.add(YearsCelebratedEvent.name, self.setup_family_tree)

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_title()
    self.builder.build_canvas()
    self.builder.build_scrollers()

    self.builder.build_legend_info()
    self.setup_family_tree()

  def setup_family_tree(self):
    self.builder.load_data_hydration()
    self.builder.build_family_tree()

  def on_deathed_person(self, data: Dict[str, Any]):
    person_id = data.get("id")
    self.widowed_person_handler.handle({ "person_id": person_id })
    self.setup_family_tree()

  def listen(self, event: Event):
    if event.name == DeathedPersonEvent.name:
      self.bus.get(event.name)(event.data)
    else:
      self.bus.get(event.name)()
