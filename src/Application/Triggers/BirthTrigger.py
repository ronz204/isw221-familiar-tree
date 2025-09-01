import random
from Domain.Models.Event import Event
from Domain.Models.Relation import Relation
from Domain.Models.Timeline import Timeline
from Database.Factory.PersonFactory import PersonFactory

from Application.Events.Broker import Broker
from Application.Triggers.Trigger import Trigger
from Application.Events.Person.PersonBornEvent import PersonBornEvent
from Application.Events.Person.NewChildrenEvent import NewChildrenEvent

class BirthTrigger(Trigger):
  def __init__(self, broker: Broker):
    super().__init__(broker)

    self.factory = PersonFactory()

  def trigger(self):
    relations = Relation.select()
    if not relations: return

    selected = random.choice(relations)

    father = selected.man
    mother = selected.woman
    emotional_compatibility = 70

    if father.emotional < emotional_compatibility: return
    if mother.emotional < emotional_compatibility: return

    child = self.factory.build(father, mother)
    child.save()

    event = Event.get(Event.name == PersonBornEvent.name)
    Timeline.create(person=child, event=event, timestamp=child.birthdate)

    event = Event.get(Event.name == NewChildrenEvent.name)
    Timeline.create(person=father, event=event, timestamp=child.birthdate)
    Timeline.create(person=mother, event=event, timestamp=child.birthdate)

    self.broker.publish(PersonBornEvent({
      "id": child.id
    }))
