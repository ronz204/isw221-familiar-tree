from typing import Dict, Any
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler
from Models.Enums.Status import Status

from Handlers.Queries.DeceasedPeople.DeceasedPeopleEvent import DeceasedPeopleEvent
from Handlers.Queries.DeceasedPeople.DeceasedPeopleSchema import DeceasedPeopleSchema

class DeceasedPeopleHandler(Handler[DeceasedPeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, DeceasedPeopleSchema)
  
  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    deceased_people = Person.select().where(
      (Person.age < 50) &
      (Person.deathdate.is_null(False)) &
      (Person.status == Status.DEATHED.value))

    deceased_list = [
      {
        "id": person.id,
        "name": person.name,
        "cedula": person.cedula,
        "age_at_death": person.age,
        "deathdate": person.deathdate.strftime("%Y-%m-%d"),
      } for person in deceased_people
    ]

    self.broker.publish(DeceasedPeopleEvent({
      "deceased": deceased_list,
    }))
