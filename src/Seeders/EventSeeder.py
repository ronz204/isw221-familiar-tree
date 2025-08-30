from typing import List
from Models.Event import Event
from Database.Seeder import Seeder
from Events.Event import Event as Ev

from Handlers.Person.BirthPerson.NewChildrenEvent import NewChildrenEvent
from Handlers.Person.BirthPerson.BirthPersonEvent import BirthPersonEvent
from Handlers.Person.DeathPerson.DeathPersonEvent import DeathPersonEvent
from Handlers.Person.CouplePerson.CouplePersonEvent import CouplePersonEvent
from Handlers.Person.DeathPerson.WidowedPersonEvent import WidowedPersonEvent
from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent
from Handlers.Person.BirthdaysPerson.BirthdaysPersonEvent import BirthdaysPersonEvent

EVENTS: List[Ev] = [
  NewChildrenEvent,
  BirthPersonEvent,
  DeathPersonEvent,
  CouplePersonEvent,
  WidowedPersonEvent,
  RegisterPersonEvent,
  BirthdaysPersonEvent,
]

class EventSeeder(Seeder):
  def seed(self) -> None:
    for event in EVENTS:
      Event.create(name=event.name, label=event.label)
