from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from Application.Events.Broker import Broker
from Application.Triggers.Trigger import Trigger

class BirthdayTrigger(Trigger):
  def __init__(self, broker: Broker):
    super().__init__(broker)

  def trigger(self):
    people = Person.select().where(Person.deathdate.is_null())

    for person in people:
      person.age += 1

      predicate1 = person.status == Status.SINGLE.value
      predicate2 = person.status == Status.WIDOWED.value

      if predicate1 or predicate2:
        if person.emotional == 0: return
        person.emotional -= 2
      person.save()
