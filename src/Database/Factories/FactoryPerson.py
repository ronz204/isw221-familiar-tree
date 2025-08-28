import random
from faker import Faker
from datetime import date
from Models.Person import Person

class FactoryPerson:
  def __init__(self) -> None:
    self.faker = Faker(locale="es_ES")

  def build(self, father: Person, mother: Person) -> Person:
    gender = random.choice(["M", "F"])
    province = random.choice([father.province, mother.province])

    cedula = str(self.faker.random_number(digits=9, fix_len=True))
    name = self.faker.first_name_male() if gender == "M" else self.faker.first_name_female()

    father_surname = father.name.split(" ")[1]
    mother_surname = mother.name.split(" ")[1]
    full_name = f"{name} {father_surname} {mother_surname}"

    return Person(
      age=0,
      name=full_name,
      cedula=cedula,
      gender=gender,
      father=father,
      mother=mother,
      guardian=mother,
      province=province,
      deathdate=None,
      birthdate=date.today())
