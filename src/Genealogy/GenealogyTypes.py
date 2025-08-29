from enum import Enum

class GenealogyTypes(Enum):
  CHILD = "Child"
  PARENT = "Parent"
  SPOUSE = "Spouse"
  SIBLING = "Sibling"

  GRANDCHILD = "Grandchild"
  GRANDPARENT = "Grandparent"

  GREAT_GRANDCHILD = "Great Grandchild"
  GREAT_GRANDPARENT = "Great Grandparent"

  COUSIN = "Cousin"
  UNCLE_AUNT = "Uncle/Aunt"
  NEPHEW_NIECE = "Nephew/Niece"
  
  NO_RELATION = "No Relation"
