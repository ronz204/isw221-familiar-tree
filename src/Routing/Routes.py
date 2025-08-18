from enum import Enum
from Views.FamilyView import FamilyView
from Views.MemberView import MemberView
from Views.RelationView import RelationView

class Routes(Enum):
  FAMILY = FamilyView
  MEMBER = MemberView
  RELATION = RelationView
