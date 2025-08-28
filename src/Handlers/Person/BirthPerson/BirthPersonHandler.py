import random
from Models.Event import Event
from Events.Broker import Broker
from typing import Dict, Any, List
from Models.Relation import Relation
from Handlers.Handler import Handler
from Models.Timeline import Timeline

from Database.Factories.FactoryPerson import FactoryPerson
from Handlers.Person.BirthPerson.BirthPersonEvent import BirthPersonEvent
from Handlers.Person.BirthPerson.NewChildrenEvent import NewChildrenEvent
from Handlers.Person.BirthPerson.BirthPersonSchema import BirthPersonSchema

class BirthPersonHandler(Handler[BirthPersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, BirthPersonSchema)
    self.factory: FactoryPerson = FactoryPerson()

  def execute(self, data: Dict[str, Any] = {}) -> None:
    validated = self.validate(data)
    if not validated: return

    relations: List[Relation] = list(Relation.select())
    if not relations: return

    selected_relation = random.choice(relations)

    father = selected_relation.man
    mother = selected_relation.woman
    min_emotional_compatibility = 70

    if father.emotional < min_emotional_compatibility: return
    if mother.emotional < min_emotional_compatibility: return

    child = self.factory.build(father, mother)
    child.save()

    child_event = Event.get(Event.name == BirthPersonEvent.name)
    Timeline.create(person_id=child.id, event_id=child_event.id, year=child.birthdate.year)

    parent_event = Event.get(Event.name == NewChildrenEvent.name)
    Timeline.create(person_id=father.id, event_id=parent_event.id, year=child.birthdate.year)
    Timeline.create(person_id=mother.id, event_id=parent_event.id, year=child.birthdate.year)

    self.broker.publish(BirthPersonEvent({
      "child_id": child.id,
      "father_id": father.id,
      "mother_id": mother.id,
    }))
