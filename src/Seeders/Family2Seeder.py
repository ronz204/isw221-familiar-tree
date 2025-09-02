from Database.Seeder import Seeder
from Models.Person import Person
from Models.Relation import Relation
from Models.Enums.Status import Status

class EventSeeder(Seeder):
  def seed(self) -> None:
    Tomas = Person.create(
      name = "Tomas Mora Ortiz",
      cedula = "1002345690",
      gender = "M",
      province = "Cartago",
      age = 75,
      birth_date = "20-08-1912",
      status = Status.DEATHED.value)
    
    Josefina = Person.create(
      name = "Josefina Solis Martinez",
      cedula = "1002345693",
      gender = "F",
      province = "Cartago",
      age = 64,
      birth_date = "15-02-1911",
      status = Status.DEATHED.value)
    
    Jacinto = Person.create(
      name = "Jacinto Mora Salazar",
      cedula = "1002345694",
      gender = "M",
      province = "Heredia",
      age = 50,
      birth_date = "25-04-1910",
      status = Status.DEATHED.value)
    
    Elena = Person.create(
      name = "Elena Rodríguez Martínez",
      cedula = "1002345689",
      gender = "F",
      province = "Cartago",
      age = 83,
      birth_date = "10-01-1915",
      status = Status.DEATHED.value)
    
    Juan = Person.create(
      name = "Juan Carlos Mora Solís",
      cedula = "1002345683",
      gender = "M",
      province = "Cartago",
      age = 83,
      birth_date = "02-05-1938",
      status = Status.DEATHED.value)
    
    Rosa = Person.create(
      name = "Rosa Chaves Jimenez",
      cedula = "1002345682",
      gender = "F",
      province = "Cartago",
      age = 80,
      birth_date = "14-01-1940",
      status = Status.DEATHED.value)
    
    Ana = Person.create(
      name = "Ana Gómez Sánchez",
      cedula = "1002345687",
      gender = "F",
      province = "Heredia ",
      age = 55,
      birth_date = "07-06-1970",
      status = Status.MARRIED.value)
    
    Diego = Person.create(
      name = "Diego Mora Sanchez",
      cedula = "1002345686",
      gender = "M",
      province = "San José",
      age = 57,
      birth_date = "12-10-1968",
      status = Status.MARRIED.value)
    
    Roberto = Person.create(
      name = "Roberto Mora Gómez",
      cedula = "1001862454",
      gender = "M",
      province = "San José",
      age = 25,
      birth_date = "10-11-2000",
      status = Status.MARRIED.value)
    
    Cristina = Person.create(
      name = "Cristina Martinez Carranza",
      cedula = "1001862111",
      gender = "F",
      province = "San José",
      age = 22,
      birth_date = "15-01-2003",
      status = Status.MARRIED.value)
    
    Luis = Person.create(
      name = "Luis Mora Martinez",
      cedula = "106520324",
      gender = "M",
      province = "Alajuela",
      age = 2,
      birth_date = "06-22-2023",
      status = Status.SINGLE.value)
    
    Carlos = Person.create(
      name = "Carlos Alberto Mora Chaves",
      cedula = "1002345679",
      gender = "M",
      province = "San José",
      age = 60,
      birth_date = "22-06-1965",
      status = Status.MARRIED.value)
    
    Carlos = Person.create(
      name = "Carlos Alberto Mora Chaves",
      cedula = "1002345679",
      gender = "M",
      province = "San José",
      age = 60,
      birth_date = "22-06-1965",
      status = Status.MARRIED.value)
    
    Manuel = Person.create(
      name = "Manuel Gómez Ruiz",
      cedula = "1002345692",
      gender = "M",
      province = "Heredia",
      age = 82,
      birth_date = "05-01-1910",
      status = Status.DEATHED.value)
    
    Clara = Person.create(
      name = "Clara Pérez López",
      cedula = "1002345695",
      gender = "F",
      province = "Alajuela",
      age = 91,
      birth_date = "23-12-1908",
      status = Status.DEATHED.value)
    
    Pedro = Person.create(
      name = "Pedro Sánchez Hernández",
      cedula = "1002345696",
      gender = "M",
      province = "Heredia",
      age = 73,
      birth_date = "12-01-1918",
      status = Status.DEATHED.value)
    
    Francisca = Person.create(
      name = "Francisca Vargas López",
      cedula = "1002345691",
      gender = "F",
      province = "Heredia",
      age = 87,
      birth_date = "12-06-1918",
      status = Status.DEATHED.value)
    
    Rafael = Person.create(
      name = "Rafael Gómez Pérez",
      cedula = "1002345685",
      gender = "M",
      province = "Heredia",
      age = 80,
      birth_date = "18-12-1939",
      status = Status.DEATHED.value)
    
    Lucia = Person.create(
      name = "Lucia Sánchez Vargas",
      cedula = "1002345684",
      gender = "F",
      province = "Heredia",
      age = 83,
      birth_date = "25-09-1942",
      status = Status.WIDOWED.value)
    
    Elena = Person.create(
      name = "Elena Gómez Sánchez",
      cedula = "1002345680",
      gender = "F",
      province = "San José",
      age = 57,
      birth_date = "30-03-1968",
      status = Status.MARRIED.value)
    
    Carlos = Person.create(
      name = "Carlos Alberto Mora Chaves",
      cedula = "1002345679",
      gender = "M",
      province = "San José",
      age = 60,
      birth_date = "22-06-1965",
      status = Status.MARRIED.value)
    
    Roney = Person.create(
      name = "Roney Porras Rojas",
      cedula = "1002220546",
      gender = "M",
      province = "San José",
      age = 40,
      birth_date = "22-04-1985",
      status = Status.MARRIED.value)
    
    Maria = Person.create(
      name = "María Mora Gomez",
      cedula = "1002345678",
      gender = "F",
      province = "San José",
      age = 35,
      birth_date = "15-04-1990",
      status = Status.MARRIED.value)
    
    Gael = Person.create(
      name = "Gael Porras Mora",
      cedula = "1001254263",
      gender = "M",
      province = "San José",
      age = 35,
      birth_date = "22-11-2018",
      status = Status.SINGLE.value)
    
    
