from typing import Dict, Any
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler

from Genealogy.GenealogyAnalyzer import GenealogyAnalyzer
from Handlers.Queries.LivingDescendants.LivingDescendantsEvent import LivingDescendantsEvent
from Handlers.Queries.LivingDescendants.LivingDescendantsSchema import LivingDescendantsSchema

class LivingDescendantsHandler(Handler[LivingDescendantsSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, LivingDescendantsSchema)
    self.analyzer = GenealogyAnalyzer()

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person = Person.get_or_none(Person.id == validated.person_id)
    if not person: return

    descendants_ids = self.analyzer.get_descendants(person)
    
    living_descendants = []
    
    for descendant_id in descendants_ids.keys():
      descendant = Person.get_or_none(Person.id == descendant_id)
      
      if descendant and descendant.deathdate is None:
        living_descendants.append({
          "id": descendant.id,
          "age": descendant.age,
          "name": descendant.name,
        })

    self.broker.publish(LivingDescendantsEvent({
      "person_id": validated.person_id,
      "living_descendants": living_descendants,
    }))
