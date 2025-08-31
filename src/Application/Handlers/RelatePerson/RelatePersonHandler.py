from Domain.Models.Person import Person

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.RelatePeopleEvent import RelatePeopleEvent
from Application.Handlers.RelatePerson.RelatePersonSchema import RelatePersonSchema

class RelatePersonHandler(Handler[RelatePersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RelatePersonSchema)

  def process(self, validated: RelatePersonSchema) -> None:
    person = Person.get_by_id(validated.person_id)
    if not person: return

    if validated.guard_id == person.id: return
    if validated.mother_id == person.id: return
    if validated.father_id == person.id: return

    if validated.guard_id:
      guard = Person.get_by_id(validated.guard_id)
      person.guard = guard

    if validated.father_id:
      father = Person.get_by_id(validated.father_id)
      person.father = father

    if validated.mother_id:
      mother = Person.get_by_id(validated.mother_id)
      person.mother = mother

    person.save()

    self.broker.publish(RelatePeopleEvent({
      "person_id": person.id,
      "guard_id": person.guard.id or None,
      "father_id": person.father.id or None,
      "mother_id": person.mother.id or None,
    }))
