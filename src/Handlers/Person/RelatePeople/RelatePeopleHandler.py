from typing import Dict, Any
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler

from Handlers.Person.RelatePeople.RelatePeopleEvent import RelatePeopleEvent
from Handlers.Person.RelatePeople.RelatePeopleSchema import RelatePeopleSchema

class RelatePeopleHandler(Handler[RelatePeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RelatePeopleSchema)

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person = Person.get_by_id(validated.person_id)
    if not person: return

    if validated.father_id == person.id: return
    if validated.mother_id == person.id: return
    if validated.guardian_id == person.id: return
    
    if validated.father_id:
      father = Person.get_by_id(validated.father_id)
      person.father = father

    if validated.mother_id:
      mother = Person.get_by_id(validated.mother_id)
      person.mother = mother

    if validated.guardian_id:
      guardian = Person.get_by_id(validated.guardian_id)
      person.guardian = guardian

    person.save()

    self.broker.publish(RelatePeopleEvent({
      "person_id": person.id,
    }))
