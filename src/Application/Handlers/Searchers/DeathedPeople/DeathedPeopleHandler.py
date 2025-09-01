from Domain.Enums.Status import Status
from Domain.Models.Person import Person

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.DeathedPeopleFoundEvent import DeathedPeopleFoundEvent
from Application.Handlers.Searchers.DeathedPeople.DeathedPeopleSchema import DeathedPeopleSchema

class DeathedPeopleHandler(Handler[DeathedPeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, DeathedPeopleSchema)

  def process(self, validated: DeathedPeopleSchema):
    deathed_people = Person.select().where(
      (Person.age < 50) &
      (Person.deathdate.is_null(False)) &
      (Person.status == Status.DEATHED.value))

    deathed_list = [
      {
        "id": person.id,
        "name": person.name,
        "cedula": person.cedula,
        "age_at_death": person.age,
        "deathdate": person.deathdate.strftime("%Y-%m-%d"),
      } for person in deathed_people
    ]

    self.broker.publish(DeathedPeopleFoundEvent({
      "deathed": deathed_list,
    }))
