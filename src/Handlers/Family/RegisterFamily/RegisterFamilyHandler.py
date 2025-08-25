from typing import Dict, Any
from Models.Family import Family
from Handlers.Handler import Handler
from Events.Family.FamilyRegisteredEvent import FamilyRegisteredEvent
from Handlers.Family.RegisterFamily.RegisterFamilySchema import RegisterFamilySchema

class RegisterFamilyHandler(Handler):
  def execute(self, data: Dict[str, Any]) -> None:
    try:
      validated = RegisterFamilySchema(**data)

      existing = Family.select().where(Family.name == validated.name).first()
      if existing: return

      family = Family.create(name=validated.name)
      self.broker.publish(FamilyRegisteredEvent({
        "id": family.id,
        "name": family.name
      }))

    except Exception as e:
      print(f"Error creating family: {e}")
