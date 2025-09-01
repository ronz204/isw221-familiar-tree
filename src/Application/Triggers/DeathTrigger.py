import random
import datetime
from Domain.Models.Event import Event
from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from Domain.Models.Timeline import Timeline
from Application.Events.Broker import Broker
from Application.Triggers.Trigger import Trigger

from Application.Events.Person.DeathedPersonEvent import DeathedPersonEvent

class DeathTrigger(Trigger):
  def __init__(self, broker: Broker):
    super().__init__(broker)

  def trigger(self):
    people = Person.select().where(Person.deathdate.is_null())
    person = random.choice(people)

    person.deathdate = datetime.datetime.now()
    person.status = Status.DEATHED.value
    person.save()

    event = Event.get(Event.name == DeathedPersonEvent.name)
    Timeline.create(person=person, event=event, timestamp=person.deathdate)

    self.broker.publish(DeathedPersonEvent({
      "id": person.id,
      "timestamp": person.deathdate,
    }))
