from typing import List
from Database.Core.Seeder import Seeder
from Domain.Enums.Affinity import Affinity as AffinityEnum
from Domain.Models.Affinity import Affinity as AffinityModel

class AffinitySeeder(Seeder):
  def seed(self) -> None:
    affinities: List[AffinityEnum] = [
      AffinityEnum.AFFI1,
      AffinityEnum.AFFI2,
      AffinityEnum.AFFI3,
      AffinityEnum.AFFI4,
      AffinityEnum.AFFI5,
      AffinityEnum.AFFI6,
      AffinityEnum.AFFI7,
    ]

    for affinity in affinities:
      AffinityModel.create(name=affinity.value)
