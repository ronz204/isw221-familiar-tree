from typing import Dict, Any
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler

from Handlers.Person.RegisterPerson.RegisterPersonEvent import RegisterPersonEvent
from Handlers.Person.RegisterPerson.RegisterPersonSchema import RegisterPersonSchema

class RegisterPersonHandler(Handler[RegisterPersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RegisterPersonSchema)

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person, created = Person.get_or_create(**validated.model_dump())
    if not created: return

    self.broker.publish(RegisterPersonEvent({
      "id": person.id,
      "name": person.name,
      "cedula": person.cedula,
      "gender": person.gender,
    }))
