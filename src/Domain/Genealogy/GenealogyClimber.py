from collections import deque
from typing import Dict, Set, Callable
from Domain.Models.Person import Person

class GenealogyClimber:
  def get_ancestors(self, person: Person) -> Dict[int, int]:
    return self.bfs(start=person.id, neighbors_func=self.get_parents)

  def get_descendants(self, person: Person) -> Dict[int, int]:
    return self.bfs(start=person.id, neighbors_func=self.get_children)

  def bfs(self, start: int, neighbors_func: Callable[[int], Set[int]]) -> Dict[int, int]:
    result: Dict[int, int] = {}
    visited: Set[int] = {start}
    queue = deque([(start, 0)])

    while queue:
      current, distance = queue.popleft()
      neighbor_ids = neighbors_func(current)

      for neighbor in neighbor_ids:
        if neighbor and neighbor not in visited:

          result[neighbor] = distance + 1
          queue.append((neighbor, distance + 1))
          visited.add(neighbor)

    return result

  def get_parents(self, person_id: int):
    person = Person.get_or_none(Person.id == person_id)
    if not person: return []
    return [person.father_id, person.mother_id]

  def get_children(self, person_id: int):
    predicate = (Person.father_id == person_id) | (Person.mother_id == person_id)
    children = Person.select().where(predicate)
    return [child.id for child in children]
