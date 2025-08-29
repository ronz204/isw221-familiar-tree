from typing import Dict, Any
from Events.Broker import Broker
from Models.Person import Person
from Handlers.Handler import Handler
from Models.Relation import Relation
from Models.Enums.Status import Status

from Handlers.Queries.ChildrenTogether.ChildrenTogetherEvent import ChildrenTogetherEvent
from Handlers.Queries.ChildrenTogether.ChildrenTogetherSchema import ChildrenTogetherSchema

class ChildrenTogetherHandler(Handler[ChildrenTogetherSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, ChildrenTogetherSchema)

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    relations = Relation.select()
    couples_with_children = []

    for relation in relations:
      if (relation.man.status == Status.MARRIED.value and 
          relation.woman.status == Status.MARRIED.value):
        
        children_count = Person.select().where(
          (Person.father == relation.man.id) &
          (Person.mother == relation.woman.id)
        ).count()

        if children_count >= 2:
          couples_with_children.append({
            "man_name": relation.man.name,
            "woman_name": relation.woman.name,
            "children_count": children_count,
          })

    self.broker.publish(ChildrenTogetherEvent({
      "couples": couples_with_children
    }))
