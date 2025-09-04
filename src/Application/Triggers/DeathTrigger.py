import random
import datetime
from typing import List
from Domain.Models.Event import Event
from Domain.Enums.Status import Status
from Domain.Models.Person import Person
from Domain.Models.Timeline import Timeline
from Application.Events.Broker import Broker
from Application.Triggers.Trigger import Trigger
from Domain.Genealogy.GenealogyTypes import GenealogyTypes
from Domain.Genealogy.GenealogyAnalyzer import GenealogyAnalyzer

from Application.Events.Person.DeathedPersonEvent import DeathedPersonEvent

class DeathTrigger(Trigger):
  def __init__(self, broker: Broker):
    super().__init__(broker)
    self.genealogy_analyzer = GenealogyAnalyzer()

  def trigger(self):
    people = Person.select().where(Person.deathdate.is_null())
    if not people: return
    
    selected_person = self.weighted_random_selection(people)
    if not selected_person: return

    minor_children = self.get_minor_children(selected_person)

    selected_person.deathdate = datetime.datetime.now()
    selected_person.status = Status.DEATHED.value
    selected_person.save()

    if minor_children:
      self.reassign_guardians(selected_person, minor_children)

    event = Event.get(Event.name == DeathedPersonEvent.name)
    Timeline.create(person=selected_person, event=event, timestamp=selected_person.deathdate)

    self.broker.publish(DeathedPersonEvent({
      "id": selected_person.id,
      "timestamp": selected_person.deathdate,
    }))

  def weighted_random_selection(self, people: List[Person]):
    if not people: return None
    weights = []

    for person in people:
      weight = 101 - person.emotional
      weights.append(weight)
  
    return random.choices(people, weights=weights, k=1)[0]

  def get_minor_children(self, person: Person) -> List[Person]:
    return list(Person.select().where(
      ((Person.mother == person.id) | (Person.father == person.id)) &
      (Person.age < 18) &
      (Person.deathdate.is_null())))

  def reassign_guardians(self, deceased_parent: Person, minor_children: List[Person]):
    for child in minor_children:
      other_parent = self.get_living_parent(child, deceased_parent)
      if other_parent: continue
      
      new_guardian = self.find_suitable_guardian(child)
      
      if new_guardian:
        child.guard_id = new_guardian.id
        child.save()

  def get_living_parent(self, child: Person, deceased_parent: Person) -> Person:
    if child.mother_id and child.mother_id != deceased_parent.id:
      mother = Person.get_by_id(child.mother_id)
      if mother and mother.deathdate is None:
        return mother
    
    if child.father_id and child.father_id != deceased_parent.id:
      father = Person.get_by_id(child.father_id)
      if father and father.deathdate is None:
        return father
    
    return None

  def find_suitable_guardian(self, child: Person) -> Person:
    potential_guardians = list(Person.select().where(
      (Person.deathdate.is_null()) &
      (Person.age >= 18) &
      (Person.id != child.id)))
    
    
    priority_relationships = [
      GenealogyTypes.GRANDPARENT,
      GenealogyTypes.UNCLE_AUNT,
      GenealogyTypes.SIBLING,
      GenealogyTypes.GREAT_GRANDPARENT,
      GenealogyTypes.COUSIN
    ]
    
    for relationship_type in priority_relationships:
      for potential_guardian in potential_guardians:
        genealogy_report = self.genealogy_analyzer.analyze(potential_guardian, child)
        
        if genealogy_report.relationship == relationship_type:
          return potential_guardian
    
    for potential_guardian in potential_guardians:
      genealogy_report = self.genealogy_analyzer.analyze(potential_guardian, child)

      if genealogy_report.relationship == GenealogyTypes.NO_RELATION:
        return potential_guardian
    
    return None
