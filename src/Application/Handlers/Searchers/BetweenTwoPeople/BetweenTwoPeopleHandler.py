from Domain.Models.Person import Person
from Domain.Genealogy.GenealogyAnalyzer import GenealogyAnalyzer

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.RelativesFoundEvent import RelativesFoundEvent
from Application.Handlers.Searchers.BetweenTwoPeople.BetweenTwoPeopleSchema import BetweenTwoPeopleSchema

class BetweenTwoPeopleHandler(Handler[BetweenTwoPeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, BetweenTwoPeopleSchema)

    self.analyzer = GenealogyAnalyzer()

  def process(self, validated: BetweenTwoPeopleSchema) -> None:
    person1 = Person.get_by_id(validated.person1_id)
    person2 = Person.get_by_id(validated.person2_id)
    if not person1 or not person2: return

    report = self.analyzer.analyze(person1, person2)

    self.broker.publish(RelativesFoundEvent({
      "distance": report.distance,
      "relation": report.relationship.value
    }))
