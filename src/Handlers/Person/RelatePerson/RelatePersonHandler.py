import datetime as dt
from typing import Dict, Any
from Models.Event import Event
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler
from Models.Timeline import Timeline

from Handlers.Person.RelatePerson.RelatePersonEvent import RelatePersonEvent
from Handlers.Person.RelatePerson.RelatePersonSchema import RelatePersonSchema

class RelatePersonHandler(Handler[RelatePersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RelatePersonSchema)

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person1: Person = Person.get_by_id(validated.person1_id)
    person2: Person = Person.get_by_id(validated.person2_id)

    if not person1 or not person2: return
    if person1.family == person2.family: return
    
    if person1.couple or person2.couple: return
    if person1.gender == person2.gender: return

    if abs(person1.age - person2.age) > 15: return
    if person1.age < 18 or person2.age < 18: return

    person1.couple = person2
    person1.save()

    person2.couple = person1
    person2.save()

    year = dt.datetime.now().year
    event = Event.get(Event.name == RelatePersonEvent.name)
    Timeline.create(person_id=person1.id, event_id=event.id, year=year)
    Timeline.create(person_id=person2.id, event_id=event.id, year=year)

    self.broker.publish(RelatePersonEvent({
      "person1_id": person1.id,
      "person1_name": person1.name,
      "person2_id": person2.id,
      "person2_name": person2.name,
    }))
