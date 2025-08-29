from Genealogy.GenealogyTypes import GenealogyTypes

class GenealogyReport:
  def __init__(self, relationship: GenealogyTypes, distance: int):
    self.relationship = relationship
    self.distance = distance
