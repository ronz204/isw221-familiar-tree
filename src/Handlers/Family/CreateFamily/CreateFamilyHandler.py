from typing import Dict, Any
from Models.Family import Family
from Handlers.Handler import Handler
from Events.EventBroker import EventBroker
from Events.Family.FamilyCreatedEvent import FamilyCreatedEvent
from Handlers.Family.CreateFamily.CreateFamilySchema import CreateFamilySchema

class CreateFamilyHandler(Handler):
  def __init__(self, broker: EventBroker):
    self.broker = broker

  def handle(self, data: Dict[str, Any]) -> None:
    try:
      validated = CreateFamilySchema(**data)

      existing = Family.select().where(Family.name == validated.name).first()
      if existing: return

      family = Family.create(name=validated.name)
      self.broker.publish(FamilyCreatedEvent({
        "id": family.id,
        "name": family.name
      }))
    except Exception as e:
      print(f"Error creating family: {e}")
