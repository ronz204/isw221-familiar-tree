from random import random
from datetime import datetime
from Models.Person import Person
from Events.Broker import Broker
from typing import Dict, Any, List
from Handlers.Handler import Handler

from Events.Person.DeathPersonEvent import DeathPersonEvent
from Handlers.Person.DeathPerson.DeathPersonSchema import DeathPersonSchema

class DeathPersonHandler(Handler[DeathPersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, DeathPersonSchema)

  def execute(self, data: Dict[str, Any] = {}) -> None:
    validated = self.validate(data)
    if not validated: return

    people: List[Person] = Person.select().where(Person.deathdate.is_null())

    for person in people:
      if random.random() < 0.05:
        person.deathdate = datetime.now()
        person.save()

        self.broker.publish(DeathPersonEvent({
          "person_id": person.id,
          "age_at_death": person.age,
          "person_name": person.name,
          "deathdate": person.deathdate.isoformat()
        }))
