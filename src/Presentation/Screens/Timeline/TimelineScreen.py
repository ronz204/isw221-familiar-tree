import tkinter as tk
from typing import Dict, Any
from Application.Events.Bus import Bus
from Application.Events.Event import Event
from Application.Events.Broker import Broker
from Application.Events.Listener import Listener

from Presentation.Screens.Timeline.TimelineBuilder import TimelineBuilder
from Application.Handlers.DisplayTimeline.DisplayTimelineHandler import DisplayTimelineHandler

from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.NewChildrenEvent import NewChildrenEvent
from Application.Events.Person.DeathedPersonEvent import DeathedPersonEvent
from Application.Events.Person.WidowedPersonEvent import WidowedPersonEvent
from Application.Events.Person.RelatedPeopleEvent import RelatedPeopleEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent
from Application.Events.Person.DisplayedTimelineEvent import DisplayedTimelineEvent

class TimelineScreen(tk.Frame, Listener):
  def __init__(self, parent: tk.Widget, broker: Broker):
    super().__init__(parent)
    self.broker: Broker = broker
    self.bus: Bus = Bus()

    self.builder = TimelineBuilder(self)
    self.display_timeline_handler = DisplayTimelineHandler(broker)

    self.setup_ui_components()
    self.subscribe_to_events()

  def subscribe_to_events(self):
    self.broker.subscribe(DisplayedTimelineEvent.name, self)
    self.broker.subscribe(RegisteredPersonEvent.name, self)
    self.broker.subscribe(PersonBornEvent.name, self)
    self.broker.subscribe(DeathedPersonEvent.name, self)
    self.broker.subscribe(WidowedPersonEvent.name, self)
    self.broker.subscribe(RelatedPeopleEvent.name, self)
    self.broker.subscribe(NewChildrenEvent.name, self)

    self.bus.add(DisplayedTimelineEvent.name, self.on_displayed_timeline)
    self.bus.add(RegisteredPersonEvent.name, self.on_person_data_changed)
    self.bus.add(PersonBornEvent.name, self.on_person_data_changed)
    self.bus.add(DeathedPersonEvent.name, self.on_person_data_changed)
    self.bus.add(WidowedPersonEvent.name, self.on_person_data_changed)
    self.bus.add(RelatedPeopleEvent.name, self.on_person_data_changed)
    self.bus.add(NewChildrenEvent.name, self.on_person_data_changed)

  def setup_ui_components(self):
    self.builder.setup_grid()
    self.builder.build_container()
    self.builder.build_frames()
    self.builder.build_title()

    self.builder.build_person_field()
    self.builder.build_search_button(self.search_command)
    
    self.builder.build_person_info_section()
    self.builder.build_timeline_section()

    self.builder.load_data_hydration()

  def search_command(self):
    data = self.builder.get_form_data()
    if data["person_id"]: self.display_timeline_handler.handle(data)

  def listen(self, event: Event):
    self.bus.get(event.name)(event.data)

  def on_displayed_timeline(self, data: Dict[str, Any]):
    timeline_data = data.get("data", {})
    timeline_events = timeline_data.get("timeline", [])
    
    self.builder.display_person_info(timeline_data)
    self.builder.display_timeline(timeline_events)

  def on_person_data_changed(self, data: Dict[str, Any]):
    self.builder.load_data_hydration()
