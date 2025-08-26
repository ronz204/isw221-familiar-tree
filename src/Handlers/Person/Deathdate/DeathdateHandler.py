import random
from datetime import datetime
from Models.Person import Person
from Handlers.Handler import Handler
from Events.Person.DeathdateEvent import DeathdateEvent

class DeathdateHandler(Handler):
  def execute(self) -> None:
    try:
      people = Person.select().where(Person.deathdate.is_null())

      for person in people:
        if random.random() < 0.05:
          person.deathdate = datetime.now()
          person.save()

          self.broker.publish(DeathdateEvent({
            "person_id": person.id,
            "person_name": person.name,
            "age_at_death": person.age,
            "deathdate": person.deathdate.isoformat()
          }))

    except Exception as e:
      print(f"Error processing deaths: {e}")
