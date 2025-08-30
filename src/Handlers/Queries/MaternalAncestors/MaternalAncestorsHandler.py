from typing import Dict, Any
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler
from Genealogy.GenealogyAnalyzer import GenealogyAnalyzer

from Handlers.Queries.MaternalAncestors.MaternalAncestorsEvent import MaternalAncestorsEvent
from Handlers.Queries.MaternalAncestors.MaternalAncestorsSchema import MaternalAncestorsSchema

class MaternalAncestorsHandler(Handler[MaternalAncestorsSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, MaternalAncestorsSchema)

    self.analyzer = GenealogyAnalyzer()

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person = Person.get_or_none(Person.id == validated.person_id)
    if not person: return

    maternal_ancestors = []

    if not person.mother_id:
      self.broker.publish(MaternalAncestorsEvent({
        "person_id": validated.person_id,
        "maternal_ancestors": maternal_ancestors,
      }))
      return
    
    mother = Person.get_or_none(Person.id == person.mother_id)

    if not mother: return
    mother_ancestors = self.analyzer.get_ancestors(mother)
    maternal_ancestors.append(mother)

    for ancestor_id in mother_ancestors.keys():
      ancestor = Person.get_or_none(Person.id == ancestor_id)
      if ancestor: maternal_ancestors.append(ancestor)
    
    ancestors_data = [
      {
        "id": ancestor.id,
        "name": ancestor.name,
      }
      for ancestor in maternal_ancestors
    ]
    
    self.broker.publish(MaternalAncestorsEvent({
      "person_id": validated.person_id,
      "maternal_ancestors": ancestors_data,
    }))
