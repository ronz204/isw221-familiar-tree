from Domain.Models.Person import Person
from Domain.Genealogy.GenealogyAnalyzer import GenealogyAnalyzer

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.DescendantsFoundAliveEvent import DescendantsFoundAliveEvent
from Application.Handlers.Searchers.LivingDescendants.LivingDescendantsSchema import LivingDescendantsSchema

class LivingDescendantsHandler(Handler[LivingDescendantsSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, LivingDescendantsSchema)

    self.analyzer = GenealogyAnalyzer()

  def process(self, validated: LivingDescendantsSchema):
    person = Person.get_by_id(validated.person_id)
    if not person: return

    descendants_ids = self.analyzer.climber.get_descendants(person)
    living_descendants = []

    for descendant_id in descendants_ids.keys():
      descendant = Person.get_or_none(Person.id == descendant_id)
      
      if descendant and descendant.deathdate is None:
        living_descendants.append({
          "id": descendant.id,
          "age": descendant.age,
          "name": descendant.name,
        })

    self.broker.publish(DescendantsFoundAliveEvent({
      "person_id": person.id,
      "descendants": living_descendants,
    }))
