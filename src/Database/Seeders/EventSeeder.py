from typing import List
from Database.Core.Seeder import Seeder
from Application.Events.Event import Event
from Domain.Models.Event import Event as Model

from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.RelatedPeopleEvent import RelatedPeopleEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent

class EventSeeder(Seeder):
  def seed(self) -> None:
    events: List[Event] = [
      PersonBornEvent,
      RelatedPeopleEvent,
      RegisteredPersonEvent,
    ]

    for event in events:
      Model.create(name=event.name, label=event.label)
