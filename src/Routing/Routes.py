from enum import Enum
from Views.FamilyView import FamilyView
from Views.MemberView import MemberView

class Routes(Enum):
  FAMILY = FamilyView
  MEMBER = MemberView
