from Domain.Models.Event import Event
from Domain.Enums.Status import Status
from Domain.Enums.Couple import Couple
from Domain.Models.Person import Person
from Domain.Models.Relation import Relation
from Domain.Models.Timeline import Timeline

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.MatchedPeopleEvent import MatchedPeopleEvent
from Application.Handlers.MatchPeople.MatchPeopleSchema import MatchPeopleSchema

class MatchPeopleHandler(Handler[MatchPeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, MatchPeopleSchema)

  def process(self, validated: MatchPeopleSchema) -> None:
    man: Person = Person.get_by_id(validated.man_id)
    if not man: return

    woman: Person = Person.get_by_id(validated.woman_id)
    if not woman: return

    if abs(man.age - woman.age) > 15: return
    if man.age < 18 or woman.age < 18: return

    Relation.create(man=man, woman=woman, timestamp=validated.timestamp)

    man.status = Status.MARRIED.value
    woman.status = Status.MARRIED.value

    man.save()
    woman.save()

    event = Event.get(Event.name == MatchedPeopleEvent.name)
    Timeline.create(person=man, event=event, timestamp=validated.timestamp)
    Timeline.create(person=woman, event=event, timestamp=validated.timestamp)

    self.broker.publish(MatchedPeopleEvent({
      "man_id": man.id,
      "woman_id": woman.id,
    }))
