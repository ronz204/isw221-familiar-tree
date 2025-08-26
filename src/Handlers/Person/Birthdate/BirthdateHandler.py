from Models.Person import Person
from Handlers.Handler import Handler
from Events.Person.BirthdateEvent import BirthdateEvent

class BirthdateHandler(Handler):
  def execute(self) -> None:
    try:
      people = Person.select().where(Person.deathdate.is_null())

      for person in people:
        person.age += 1
        person.save()

        self.broker.publish(BirthdateEvent({
          "person_id": person.id,
          "person_name": person.name,
          "new_age": person.age
        }))

    except Exception as e:
      print(f"Error birthdate people: {e}")
