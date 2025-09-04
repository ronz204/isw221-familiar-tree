from Domain.Models.Event import Event
from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from Domain.Models.Relation import Relation
from Domain.Models.Timeline import Timeline
from Domain.Genealogy.GenealogyTypes import GenealogyTypes
from Domain.Genealogy.GenealogyAnalyzer import GenealogyAnalyzer

from Application.Events.Broker import Broker
from Application.Handlers.Handler import Handler
from Application.Events.Person.MatchedPeopleEvent import MatchedPeopleEvent
from Application.Handlers.MatchPeople.MatchPeopleSchema import MatchPeopleSchema

class MatchPeopleHandler(Handler[MatchPeopleSchema]):
  def __init__(self, broker: Broker):
    super().__init__(broker, MatchPeopleSchema)
    self.genealogy_analyzer = GenealogyAnalyzer()

  def process(self, validated: MatchPeopleSchema) -> None:
    man: Person = Person.get_by_id(validated.man_id)
    if not man: return

    woman: Person = Person.get_by_id(validated.woman_id)
    if not woman: return

    if abs(man.age - woman.age) > 15: return
    if man.age < 18 or woman.age < 18: return
    
    if not self.are_compatible(man, woman): return
    if self.has_family_relationship(man, woman): return

    Relation.create(man=man, woman=woman, timestamp=validated.timestamp)

    if man.status != Status.DEATHED.value:
      man.status = Status.MARRIED.value
    
    if woman.status != Status.DEATHED.value:
      woman.status = Status.MARRIED.value

    man.save()
    woman.save()

    event = Event.get(Event.name == MatchedPeopleEvent.name)
    Timeline.create(person=man, event=event, timestamp=validated.timestamp)
    Timeline.create(person=woman, event=event, timestamp=validated.timestamp)

    self.broker.publish(MatchedPeopleEvent({
      "man_id": man.id,
      "woman_id": woman.id,
    }))

  def are_compatible(self, man: Person, woman: Person) -> bool:
    man_passions = set(p.affinity.id for p in man.passions)
    woman_passions = set(p.affinity.id for p in woman.passions)
    
    passion_diff = abs(len(man_passions) - len(woman_passions))
    if passion_diff > 1: return False
    
    min_passions = min(len(man_passions), len(woman_passions))
    if min_passions == 0: return False

    common_passions = man_passions.intersection(woman_passions)
    compatibility_percentage = (len(common_passions) / min_passions) * 100
    
    if compatibility_percentage >= 70: return True
    return False

  def has_family_relationship(self, man: Person, woman: Person) -> bool:
    genealogy_report = self.genealogy_analyzer.analyze(man, woman)
    if genealogy_report.relationship == GenealogyTypes.NO_RELATION: return False
    return True
