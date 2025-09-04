from Domain.Models.Event import Event
from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from Domain.Models.Passions import Passions
from Domain.Models.Timeline import Timeline
from Domain.Models.Affinity import Affinity

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.RegisteredPersonEvent import RegisteredPersonEvent
from Application.Handlers.RegisterPerson.RegisterPersonSchema import RegisterPersonSchema

class RegisterPersonHandler(Handler[RegisterPersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RegisterPersonSchema)

  def process(self, validated: RegisterPersonSchema) -> None:
    data = validated.model_dump()
    affinity_ids = data.pop("affinities", [])

    if data.get("deathdate"):
      data["status"] = Status.DEATHED.value
    
    person, created = Person.get_or_create(**data)
    if not created: return

    for affinity_id in affinity_ids:
      affinity = Affinity.get_by_id(affinity_id)
      Passions.create(person=person, affinity=affinity)

    event = Event.get(Event.name == PersonBornEvent.name)
    Timeline.create(event=event, person=person, timestamp=data["birthdate"])

    self.broker.publish(PersonBornEvent({
      "id": person.id,
      "name": person.name,
    }))

    self.broker.publish(RegisteredPersonEvent({
      "id": person.id,
      "name": person.name,
      "cedula": person.cedula,
    }))
