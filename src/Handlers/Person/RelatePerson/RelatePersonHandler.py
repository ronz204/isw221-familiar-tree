from typing import Dict, Any
from Models.Event import Event
from Models.Person import Person
from Models.Relation import Relation
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
    if person1.gender == person2.gender: return

    if abs(person1.age - person2.age) > 15: return
    if person1.age < 18 or person2.age < 18: return

    Relation.create(person1=person1, person2=person2, year=validated.year)

    event = Event.get(Event.name == RelatePersonEvent.name)
    Timeline.create(person_id=person1.id, event_id=event.id, year=validated.year)
    Timeline.create(person_id=person2.id, event_id=event.id, year=validated.year)

    self.broker.publish(RelatePersonEvent({
      "year": validated.year,
      "person1_id": person1.id,
      "person1_name": person1.name,
      "person2_id": person2.id,
      "person2_name": person2.name,
    }))
