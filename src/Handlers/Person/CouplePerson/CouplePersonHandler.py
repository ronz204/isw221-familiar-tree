from typing import Dict, Any
from Models.Event import Event
from Models.Person import Person
from Events.Broker import Broker
from Models.Relation import Relation
from Handlers.Handler import Handler
from Models.Timeline import Timeline
from Models.Enums.Status import Status

from Handlers.Person.CouplePerson.CouplePersonEvent import CouplePersonEvent
from Handlers.Person.CouplePerson.CouplePersonSchema import CouplePersonSchema

class CouplePersonHandler(Handler[CouplePersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, CouplePersonSchema)

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    man: Person = Person.get_by_id(validated.man_id)
    woman: Person = Person.get_by_id(validated.woman_id)

    if abs(man.age - woman.age) > 15: return
    if man.age < 18 or woman.age < 18: return

    Relation.create(man=man, woman=woman, year=validated.year)

    man.status = Status.MARRIED.value
    woman.status = Status.MARRIED.value

    man.save()
    woman.save()

    event = Event.get(Event.name == CouplePersonEvent.name)
    Timeline.create(person_id=man.id, event_id=event.id, year=validated.year)
    Timeline.create(person_id=woman.id, event_id=event.id, year=validated.year)

    self.broker.publish(CouplePersonEvent({
      "year": validated.year,
      "man_id": man.id,
      "man_name": man.name,
      "woman_id": woman.id,
      "woman_name": woman.name,
    }))
