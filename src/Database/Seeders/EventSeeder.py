from typing import List
from Models.Event import Event
from Database.Seeder import Seeder
from Events.Event import Event as Ev

from Handlers.Person.DeathPerson.DeathPersonEvent import DeathPersonEvent
from Handlers.Person.RelateCouple.RelateCoupleEvent import RelateCoupleEvent
from Handlers.Family.RegisterFamily.RegisterFamilyEvent import RegisterFamilyEvent
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent
from Handlers.Person.BirthdaysPerson.BirthdaysPersonEvent import BirthdaysPersonEvent

EVENTS: List[Ev] = [
  DeathPersonEvent,
  RelateCoupleEvent,
  RegisterFamilyEvent,
  RegisterPersonEvent,
  BirthdaysPersonEvent,
]

class EventSeeder(Seeder):
  def seed(self) -> None:
    for event in EVENTS:
      Event.create(name=event.name, label=event.label)
