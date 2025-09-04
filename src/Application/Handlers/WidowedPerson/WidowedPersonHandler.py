from Domain.Models.Event import Event
from Domain.Enums.Couple import Couple
from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from Domain.Models.Relation import Relation
from Domain.Models.Timeline import Timeline

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.WidowedPersonEvent import WidowedPersonEvent
from Application.Handlers.WidowedPerson.WidowedPersonSchema import WidowedPersonSchema

class WidowedPersonHandler(Handler[WidowedPersonSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, WidowedPersonSchema)

  def process(self, validated: WidowedPersonSchema) -> None:
    person = Person.get_by_id(validated.person_id)
    if not person: return

    predicate1 = (Relation.man == person)
    predicate2 = (Relation.woman == person)

    relation = Relation.get_or_none(predicate1 | predicate2)
    if not relation: return

    couple = relation.woman if relation.man == person else relation.man
    relation.status = Couple.PREVIOUS.value
    
    couple.status = Status.WIDOWED.value
    couple.emotional -= 10

    couple.save()
    relation.save()

    event = Event.get(Event.name == WidowedPersonEvent.name)
    Timeline.create(person=couple, event=event, timestamp=person.deathdate)
