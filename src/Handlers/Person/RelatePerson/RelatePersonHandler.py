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

    man: Person = Person.get_by_id(validated.man_id)
    woman: Person = Person.get_by_id(validated.woman_id)

    if not man or not woman: return
    if man.gender == woman.gender: return

    if abs(man.age - woman.age) > 15: return
    if man.age < 18 or woman.age < 18: return

    Relation.create(man=man, woman=woman, year=validated.year)

    event = Event.get(Event.name == RelatePersonEvent.name)
    Timeline.create(person_id=man.id, event_id=event.id, year=validated.year)
    Timeline.create(person_id=woman.id, event_id=event.id, year=validated.year)

    self.broker.publish(RelatePersonEvent({
      "year": validated.year,
      "man_id": man.id,
      "man_name": man.name,
      "woman_id": woman.id,
      "woman_name": woman.name,
    }))
