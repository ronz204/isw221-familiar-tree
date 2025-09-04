import random
import datetime
from typing import List
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
    if not people: return
    
    selected_person = self.weighted_random_selection(people)
    if not selected_person:return

    selected_person.deathdate = datetime.datetime.now()
    selected_person.status = Status.DEATHED.value
    selected_person.save()

    event = Event.get(Event.name == DeathedPersonEvent.name)
    Timeline.create(person=selected_person, event=event, timestamp=selected_person.deathdate)

    self.broker.publish(DeathedPersonEvent({
      "id": selected_person.id,
      "timestamp": selected_person.deathdate,
    }))

  def weighted_random_selection(self, people: List[Person]):
    if not people: return None
    weights = []

    for person in people:
      weight = 101 - person.emotional
      weights.append(weight)
  
    return random.choices(people, weights=weights, k=1)[0]
