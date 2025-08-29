from typing import Dict, Any
from Models.Person import Person
from Events.Broker import Broker
from Handlers.Handler import Handler

from Genealogy.GenealogyAnalyzer import GenealogyAnalyzer
from Handlers.Queries.BetweenPeople.BetweenPeopleEvent import BetweenPeopleEvent
from Handlers.Queries.BetweenPeople.BetweenPeopleSchema import BetweenPeopleSchema

class BetweenPeopleHandler(Handler[BetweenPeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, BetweenPeopleSchema)

    self.analyzer = GenealogyAnalyzer()

  def execute(self, data: Dict[str, Any]) -> None:
    validated = self.validate(data)
    if not validated: return

    person1 = Person.get_by_id(validated.person1)
    person2 = Person.get_by_id(validated.person2)

    if not person1 or not person2: return

    report = self.analyzer.analyze(person1, person2)
    print(f"Relationship between {person1.name} and {person2.name}: {report.relationship.value}")

    self.broker.publish(BetweenPeopleEvent({
      "distance": report.distance,
      "relationship": report.relationship.value,
    }))
