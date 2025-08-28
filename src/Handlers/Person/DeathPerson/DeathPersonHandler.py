import random
from datetime import datetime
from Models.Event import Event
from Models.Person import Person
from Events.Broker import Broker
from typing import Dict, Any, List
from Handlers.Handler import Handler
from Models.Timeline import Timeline
from Models.Relation import Relation
from Models.Enums.Status import Status

from Handlers.Person.DeathPerson.DeathPersonEvent import DeathPersonEvent
from Handlers.Person.DeathPerson.DeathPersonSchema import DeathPersonSchema
from Handlers.Person.DeathPerson.WidowedPersonEvent import WidowedPersonEvent

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
        person.status = Status.DEATHED.value
        
        year = person.deathdate.year
        person.save()

        self.handle_widowed_couple(person, year)
        death_event = Event.get(Event.name == DeathPersonEvent.name)
        Timeline.create(person_id=person.id, event_id=death_event.id, year=year)

        self.broker.publish(DeathPersonEvent({
          "person_id": person.id,
          "age_at_death": person.age,
          "person_name": person.name,
          "deathdate": person.deathdate.isoformat()
        }))
  
  def handle_widowed_couple(self, person: Person, year: int):
    relation = Relation.get_or_none((Relation.man == person) | (Relation.woman == person))
    if not relation: return

    couple = relation.woman if relation.man == person else relation.man
    couple.status = Status.WIDOWED.value
    couple.save()

    widowed_event = Event.get(Event.name == WidowedPersonEvent.name)
    Timeline.create(person_id=couple.id, event_id=widowed_event.id, year=year)
