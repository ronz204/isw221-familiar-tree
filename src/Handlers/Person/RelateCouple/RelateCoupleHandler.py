from typing import Dict, Any
from Models.Person import Person
from Handlers.Handler import Handler
from Events.Person.CoupleRelatedEvent import CoupleRelatedEvent
from Handlers.Person.RelateCouple.RelateCoupleSchema import RelateCoupleSchema

class RelateCoupleHandler(Handler):
  def execute(self, data: Dict[str, Any]) -> None:
    try:
      validated = RelateCoupleSchema(**data)

      person1 = Person.get_by_id(validated.person1_id)
      person2 = Person.get_by_id(validated.person2_id)

      if not person1 or not person2: return
      if person1.couple or person2.couple: return
      if person1.gender == person2.gender: return

      if abs(person1.age - person2.age) > 15: return
      if person1.age < 18 or person2.age < 18: return

      person1.couple = person2
      person1.save()

      person2.couple = person1
      person2.save()

      self.broker.publish(CoupleRelatedEvent({
        "person1_id": person1.id,
        "person1_name": person1.name,
        "person2_id": person2.id,
        "person2_name": person2.name,
      }))

    except Exception as e:
      print(f"Error relating couple: {e}")