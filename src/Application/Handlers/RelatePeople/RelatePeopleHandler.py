from Domain.Models.Event import Event
from Domain.Models.Person import Person
from Domain.Models.Timeline import Timeline

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.NewChildrenEvent import NewChildrenEvent
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

      event = Event.get(Event.name == NewChildrenEvent.name)
      Timeline.create(event=event, person=father, timestamp=person.birthdate)

    if validated.mother_id:
      mother = Person.get_by_id(validated.mother_id)
      person.mother = mother

      event = Event.get(Event.name == NewChildrenEvent.name)
      Timeline.create(event=event, person=mother, timestamp=person.birthdate)

    person.save()

    self.broker.publish(RelatedPeopleEvent({
      "person_id": person.id,
    }))
