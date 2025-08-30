from typing import Dict, Set
from collections import deque
from Models.Person import Person
from Models.Relation import Relation
from Genealogy.GenealogyTypes import GenealogyTypes
from Genealogy.GenealogyReport import GenealogyReport

class GenealogyAnalyzer:
  def analyze(self, person1: Person, person2: Person) -> GenealogyReport:
    if person1.id == person2.id: return GenealogyReport(GenealogyTypes.NO_RELATION, 0)

    relationship = self.check_direct_relationship(person1, person2)
    if relationship != GenealogyTypes.NO_RELATION:
      return GenealogyReport(relationship, 1)

    return self.check_extended_relationship(person1, person2)

  def check_direct_relationship(self, person1: Person, person2: Person) -> GenealogyTypes:
    if person1.id == person2.father_id or person1.id == person2.mother_id:
      return GenealogyTypes.PARENT
    
    if person1.father_id == person2.id or person1.mother_id == person2.id:
      return GenealogyTypes.CHILD

    same_father = person1.father_id == person2.father_id and person1.father_id is not None
    same_mother = person1.mother_id == person2.mother_id and person1.mother_id is not None
    if same_father or same_mother: return GenealogyTypes.SIBLING

    relation_exists = Relation.select().where(
      ((Relation.man == person1.id) & (Relation.woman == person2.id)) |
      ((Relation.man == person2.id) & (Relation.woman == person1.id))
    ).exists()

    if relation_exists: return GenealogyTypes.SPOUSE
    return GenealogyTypes.NO_RELATION

  def check_extended_relationship(self, person1: Person, person2: Person) -> GenealogyReport:
    ancestors1 = self.get_ancestors(person1)
    ancestors2 = self.get_ancestors(person2)

    if person1.id in ancestors2:
      distance = ancestors2[person1.id]
      if distance == 2: return GenealogyReport(GenealogyTypes.GRANDPARENT, 2)
      if distance == 3: return GenealogyReport(GenealogyTypes.GREAT_GRANDPARENT, 3)

    if person2.id in ancestors1:
      distance = ancestors1[person2.id]
      if distance == 2: return GenealogyReport(GenealogyTypes.GRANDCHILD, 2)
      if distance == 3: return GenealogyReport(GenealogyTypes.GREAT_GRANDCHILD, 3)

    common_ancestors = set(ancestors1.keys()) & set(ancestors2.keys())
    if not common_ancestors: return GenealogyReport(GenealogyTypes.NO_RELATION, -1)

    closest = min(common_ancestors, key=lambda x: ancestors1[x] + ancestors2[x])
    dist1, dist2 = ancestors1[closest], ancestors2[closest]

    if dist1 == 1 and dist2 == 2: return GenealogyReport(GenealogyTypes.UNCLE_AUNT, 3)
    if dist1 == 2 and dist2 == 1: return GenealogyReport(GenealogyTypes.NEPHEW_NIECE, 3)
    if dist1 == 2 and dist2 == 2: return GenealogyReport(GenealogyTypes.COUSIN, 4)

    return GenealogyReport(GenealogyTypes.NO_RELATION, -1)

  def get_ancestors(self, person: Person) -> Dict[int, int]:
    ancestors: Dict[int, int] = {}
    visited: Set[int] = {person.id}

    queue = deque([(person.id, 0)])

    while queue:
      current_id, distance = queue.popleft()

      try:
        current = Person.get_by_id(current_id)

        for parent_id in [current.father_id, current.mother_id]:
          if parent_id and parent_id not in visited:
            ancestors[parent_id] = distance + 1
            queue.append((parent_id, distance + 1))
            visited.add(parent_id)

      except:
        continue

    return ancestors

  def get_descendants(self, person: Person) -> Dict[int, int]:
    descendants: Dict[int, int] = {}
    visited: Set[int] = {person.id}

    queue = deque([(person.id, 0)])

    while queue:
      current_id, distance = queue.popleft()

      try:
        predicate = (Person.father_id == current_id) | (Person.mother_id == current_id)
        children = Person.select().where(predicate)

        for child in children:
          if child.id not in visited:
            descendants[child.id] = distance + 1
            queue.append((child.id, distance + 1))
            visited.add(child.id)

      except:
        continue

    return descendants
