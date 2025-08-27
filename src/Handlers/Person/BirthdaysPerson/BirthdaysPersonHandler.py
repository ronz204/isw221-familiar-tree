from Models.Person import Person
from Events.Broker import Broker
from typing import Dict, Any, List
from Handlers.Handler import Handler

from Handlers.Person.BirthdaysPerson.BirthdaysPersonEvent import BirthdaysPersonEvent
from Handlers.Person.BirthdaysPerson.BirthdaysPersonSchema import BirthdaysPersonSchema

class BirthdaysPersonHandler(Handler[BirthdaysPersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, BirthdaysPersonSchema)

  def execute(self, data: Dict[str, Any] = {}) -> None:
    validated = self.validate(data)
    if not validated: return

    people: List[Person] = Person.select().where(Person.deathdate.is_null())

    for person in people:
      person.age += 1
      person.save()

      self.broker.publish(BirthdaysPersonEvent({
        "id": person.id,
        "age": person.age,
        "name": person.name,
      }))
