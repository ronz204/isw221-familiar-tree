from Models.Person import Person
from Events.Broker import Broker
from typing import Dict, Any, List
from Handlers.Handler import Handler

from Genealogy.GenealogyTypes import GenealogyTypes
from Genealogy.GenealogyAnalyzer import GenealogyAnalyzer
from Handlers.Queries.FirstGradeCousins.FirstGradeCousinsEvent import FirstGradeCousinsEvent
from Handlers.Queries.FirstGradeCousins.FirstGradeCousinsSchema import FirstGradeCousinsSchema

class FirstGradeCousinsHandler(Handler[FirstGradeCousinsSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, FirstGradeCousinsSchema)

    self.analyzer = GenealogyAnalyzer()

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person = Person.get_by_id(validated.person_id)
    if not person: return

    cousins: List[Person] = []

    for candidate in Person.select():
      if candidate.id == person.id: continue

      report = self.analyzer.analyze(person, candidate)
      if report.relationship == GenealogyTypes.COUSIN:
        cousins.append(candidate)

    self.broker.publish(FirstGradeCousinsEvent({
      "cousins": cousins,
      "person_id": person.id,
      "person_name": person.name,
    }))
