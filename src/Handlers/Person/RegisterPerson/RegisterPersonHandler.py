from typing import Dict, Any
from Models.Event import Event
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler
from Models.Timeline import Timeline
from Models.Enums.Status import Status

from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent
from Handlers.Person.RegisterPerson.RegisterPersonSchema import RegisterPersonSchema

class RegisterPersonHandler(Handler[RegisterPersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RegisterPersonSchema)

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person_data = validated.model_dump()

    if person_data.get("deathdate"):
      person_data["status"] = Status.DEATHED.value

    person, created = Person.get_or_create(**person_data)
    if not created: return

    year = person.birthdate.year
    event = Event.get(Event.name == RegisterPersonEvent.name)
    Timeline.create(person_id=person.id, event_id=event.id, year=year)

    self.broker.publish(RegisterPersonEvent({
      "id": person.id,
      "name": person.name,
      "cedula": person.cedula,
      "gender": person.gender,
    }))
