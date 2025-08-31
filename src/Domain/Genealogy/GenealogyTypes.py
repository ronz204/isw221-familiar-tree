from enum import Enum

class GenealogyTypes(Enum):
  CHILD = "Hijos"
  PARENT = "Padres"
  SPOUSE = "Esposos"
  SIBLING = "Hermanos"

  GRANDCHILD = "Nietos"
  GRANDPARENT = "Abuelos"

  GREAT_GRANDCHILD = "Bisnietos"
  GREAT_GRANDPARENT = "Bisabuelos"

  COUSIN = "Primos"
  UNCLE_AUNT = "Tíos"
  NEPHEW_NIECE = "Sobrinos"
  
  NO_RELATION = "No Relacionados"
