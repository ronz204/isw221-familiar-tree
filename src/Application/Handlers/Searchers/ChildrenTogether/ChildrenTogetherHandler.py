from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from Domain.Models.Relation import Relation

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.ChildrenTogetherFoundEvent import ChildrenTogetherFoundEvent
from Application.Handlers.Searchers.ChildrenTogether.ChildrenTogetherSchema import ChildrenTogetherSchema

class ChildrenTogetherHandler(Handler[ChildrenTogetherSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, ChildrenTogetherSchema)

  def process(self, validated: ChildrenTogetherSchema):
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

    self.broker.publish(ChildrenTogetherFoundEvent({
      "couples": couples_with_children
    }))
