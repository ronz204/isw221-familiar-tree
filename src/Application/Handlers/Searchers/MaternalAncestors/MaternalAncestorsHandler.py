from Domain.Models.Person import Person
from Domain.Genealogy.GenealogyAnalyzer import GenealogyAnalyzer

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.MaternalAncestorsFoundEvent import MaternalAncestorsFoundEvent
from Application.Handlers.Searchers.MaternalAncestors.MaternalAncestorsSchema import MaternalAncestorsSchema

class MaternalAncestorsHandler(Handler):
  def __init__(self, broker: Broker):
    super().__init__(broker, MaternalAncestorsSchema)

    self.analyzer = GenealogyAnalyzer()

  def process(self, validated: MaternalAncestorsSchema):
    person = Person.get_by_id(validated.person_id)
    if not person: return
    ancestors = []

    if not person.mother_id:
      self.broker.publish(MaternalAncestorsFoundEvent({
        "person_id": person.id,
        "ancestors": ancestors,
      }))
      return
  
    mother = Person.get_by_id(person.mother_id)
    if not mother: return

    mother_ancestors = self.analyzer.climber.get_ancestors(mother)
    ancestors.append(mother)

    for ancestor_id in mother_ancestors.keys():
      ancestor = Person.get_or_none(Person.id == ancestor_id)
      if ancestor: ancestors.append(ancestor)
    
    ancestors_data = [
      {
        "id": ancestor.id,
        "name": ancestor.name,
      }
      for ancestor in ancestors
    ]

    self.broker.publish(MaternalAncestorsFoundEvent({
      "person_id": person.id,
      "ancestors": ancestors_data,
    }))
