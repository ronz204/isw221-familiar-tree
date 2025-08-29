from collections import deque
from Models.Person import Person
from Models.Relation import Relation
from typing import Optional, Dict, List
from Genealogy.GenealogyTypes import GenealogyTypes
from Genealogy.GenealogyReport import GenealogyReport

class GenealogyAnalyzer:
  def analyze(self, person1: Person, person2: Person) -> GenealogyReport:
    if person1.id == person2.id: return GenealogyReport(GenealogyTypes.NO_RELATION, 0)

    relationship = self.check_direct_relationship(person1, person2)
    if relationship != GenealogyTypes.NO_RELATION: return GenealogyReport(relationship, 1)

  def check_direct_relationship(self, person1: Person, person2: Person) -> GenealogyTypes:
    if person1.id == person2.father_id or person1.id == person2.mother_id:
      return GenealogyTypes.PARENT
    
    if person1.father_id == person2.id or person1.mother_id == person2.id:
      return GenealogyTypes.CHILD

    same_father = person1.father_id == person2.father_id and person1.father_id is not None and person2.father_id is not None
    same_mother = person1.mother_id == person2.mother_id and person1.mother_id is not None and person2.mother_id is not None
    if same_father or same_mother: return GenealogyTypes.SIBLING

    relation_exists = Relation.select().where(
      ((Relation.man == person1.id) & (Relation.woman == person2.id)) |
      ((Relation.man == person2.id) & (Relation.woman == person1.id))
    ).exists()

    if relation_exists: return GenealogyTypes.SPOUSE

    return GenealogyTypes.NO_RELATION
