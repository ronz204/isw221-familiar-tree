from typing import Dict, Any
from Models.Family import Family
from Events.Broker import Broker
from Handlers.Handler import Handler

from Handlers.Family.RegisterFamily.RegisterFamilyEvent import RegisterFamilyEvent
from Handlers.Family.RegisterFamily.RegisterFamilySchema import RegisterFamilySchema

class RegisterFamilyHandler(Handler[RegisterFamilySchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, RegisterFamilySchema)

  def execute(self, data: Dict[str, Any]):
    validated = self.validate(data)
    if not validated: return

    family, created = Family.get_or_create(**validated.model_dump())
    if not created: return

    self.broker.publish(RegisterFamilyEvent({
      "id": family.id,
      "name": family.name
    }))
