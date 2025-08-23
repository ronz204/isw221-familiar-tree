from typing import Dict, Any
from Models.Person import Person
from Handlers.Handler import Handler
from Events.EventBroker import EventBroker
from Events.Person.PersonRegisteredEvent import PersonRegisteredEvent
from Handlers.Person.RegisterPerson.RegisterPersonSchema import RegisterPersonSchema

class RegisterPersonHandler(Handler):
  def __init__(self, broker: EventBroker):
    self.broker = broker

  def handle(self, data: Dict[str, Any]) -> None:
    try:
      validated = RegisterPersonSchema(**data)

      existing = Person.select().where(Person.cedula == validated.cedula).first()
      if existing: return

      person = Person.create(
        name=validated.name,
        cedula=validated.cedula,
        gender=validated.gender,
        province=validated.province,
        emotional=validated.emotional,
        age=validated.age,
        birthdate=validated.birthdate,
        deathdate=validated.deathdate,
        family=validated.family_id,
        mother=validated.mother_id,
        father=validated.father_id,
      )

      self.broker.publish(PersonRegisteredEvent({
        "id": person.id,
        "name": person.name,
        "cedula": person.cedula,
        "gender": person.gender,
      }))
    except Exception as e:
      print(f"Error creating person: {e}")
