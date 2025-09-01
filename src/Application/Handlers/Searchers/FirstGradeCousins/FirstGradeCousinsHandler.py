from typing import List
from Domain.Models.Person import Person
from Domain.Genealogy.GenealogyTypes import GenealogyTypes
from Domain.Genealogy.GenealogyAnalyzer import GenealogyAnalyzer

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.CousinsFoundEvent import CousinsFoundEvent
from Application.Handlers.Searchers.FirstGradeCousins.FirstGradeCousinsSchema import FirstGradeCousinsSchema

class FirstGradeCousinsHandler(Handler[FirstGradeCousinsSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, FirstGradeCousinsSchema)

    self.analyzer = GenealogyAnalyzer()

  def process(self, validated: FirstGradeCousinsSchema):
    person = Person.get_by_id(validated.person_id)
    if not person: return

    cousins: List[Person] = []
    for candidate in Person.select():
      if candidate.id == person.id: continue

      report = self.analyzer.analyze(person, candidate)
      if report.relationship == GenealogyTypes.COUSIN:
        cousins.append(candidate)

    self.broker.publish(CousinsFoundEvent({
      "cousins": cousins,
      "person_id": person.id,
    }))
