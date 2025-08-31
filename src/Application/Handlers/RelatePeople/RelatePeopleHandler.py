from Domain.Models.Person import Person

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.RelatedPeopleEvent import RelatedPeopleEvent
from Application.Handlers.RelatePeople.RelatePeopleSchema import RelatePeopleSchema

class RelatePeopleHandler(Handler[RelatePeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RelatePeopleSchema)

  def process(self, validated: RelatePeopleSchema) -> None:
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

    self.broker.publish(RelatedPeopleEvent({
      "person_id": person.id,
    }))
