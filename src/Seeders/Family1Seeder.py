from Database.Seeder import Seeder
from Models.Person import Person
from Models.Relation import Relation
from Models.Enums.Status import Status

class EventSeeder(Seeder):
  def seed(self) -> None:
    Roberto = Person.create(
      name = "Roberto Herrera Fallas",
      cedula = "101210527",
      gender = "M",
      province = "San José",
      age = 83,
      birth_date = "07-01-1917",
      status = Status.DEATHED.value)
    
    Blanca = Person.create(
      name = "Blanca Rosa Valverde Nuñez",
      cedula = "102770557",
      gender = "F",
      province = "San José",
      age = 79,
      birth_date = "09-10-1936",
      status = Status.DEATHED.value)
    
    Hector = Person.create(
      name = "Hector Chacón Vargas",
      cedula = "102660980",
      gender = "M",
      province = "San José",
      age = 87,
      birth_date = "02-08-1938",
      status = Status.WIDOWED.value)
    
    Esperanza = Person.create(
      name = "Esperanza Anabel Cascante Muñoz",
      cedula = "102860594",
      gender = "F",
      province = "San José",
      age = 65,
      birth_date = "19-08-1940",
      status = Status.DEATHED.value)
    
    Ulises = Person.create(
      name = "Ulises Jose Herrera Valverde",
      cedula = "901030815",
      gender = "M",
      province = "Pérez Zeledón",
      age = 70,
      birth_date = "11-09-1955",
      status = Status.WIDOWED.value)
    
    Damaris = Person.create(
      name = "María Damaris Genarina Chacón Cascante",
      cedula = "105520387",
      gender = "F",
      province = "San José",
      age = 60,
      birth_date = "25-12-1960",
      status = Status.DEATHED.value)
    
    Damaris = Person.create(
      name = "María Damaris Genarina Chacón Cascante",
      cedula = "105520387",
      gender = "F",
      province = "San José",
      age = 60,
      birth_date = "25-12-1960",
      status = Status.DEATHED.value)
    
    Iabell = Person.create(
      name = "Isabell Herrera Chacón",
      cedula = "207180676",
      gender = "F",
      province = "Alajuela",
      age = 31,
      birth_date = "14-10-1993",
      status = Status.MARRIED.value)
    
    Cesar = Person.create(
      name = "Cesar Padilla Morales",
      cedula = "105210213",
      gender = "M",
      province = "San José",
      age = 43,
      birth_date = "15-01-1982",
      status = Status.MARRIED.value)
    
    Isabell = Person.create(
      name = "Isabella Padilla Herrera",
      cedula = "115870654",
      gender = "F",
      province = "San José",
      age = 7,
      birth_date = "12-07-2018",
      status = Status.SINGLE.value)
    
    Tiffany = Person.create(
      name = "Tifanny Padilla Herrera",
      cedula = "11230213",
      gender = "F",
      province = "San José",
      age = 15,
      birth_date = "25-12-2010",
      status = Status.SINGLE.value)
    
    Johanny = Person.create(
      name = "Johanny Herrera Chacón",
      cedula = "109490818",
      gender = "M",
      province = "San José",
      age = 49,
      birth_date = "15-07-1976",
      status = Status.MARRIED.value)
      
    Delfin = Person.create(
      name = "Deflin Carvajal Fonseca",
      cedula = "202380438",
      gender = "M",
      province = "Alajuela",
      age = 67,
      birth_date = "24-08-1945",
      status = Status.DEATHED.value)
    
    Elida = Person.create(
      name = "Elida Cubero Salas",
      cedula = "205580438",
      gender = "F",
      province = "Alajuela",
      age = 67,
      birth_date = "24-08-1945",
      status = Status.DEATHED.value)
    
    Amando = Person.create(
      name = "Amando Benavides Calvo",
      cedula = "202380458",
      gender = "M",
      province = "Alajuela",
      age = 67,
      birth_date = "14-05-1945",
      status = Status.DEATHED.value)
    
    Juaquín = Person.create(
      name = "JuaquÍn Carvajal Cubero",
      cedula = "202980431",
      gender = "M",
      province = "Alajuela",
      age = 67,
      birth_date = "24-08-1945",
      status = Status.DEATHED.value)

    Nelly = Person.create(
      name = "Nelly Benavides Jimenez",
      cedula = "202840627",
      gender = "F",
      province = "Alajuela",
      age = 73,
      birth_date = "08-07-1952",
      status = Status.WIDOWED.value)
    
    Maria = Person.create(
      name = "María Carvajal Benavidez",
      cedula = "205080925",
      gender = "F",
      province = "Alajuela",
      age = 49,
      birth_date = "15-02-1976",
      status = Status.MARRIED.value)
    
    Carmen = Person.create(
      name = "Carmen Carvajal Benavidez",
      cedula = "201220125",
      gender = "F",
      province = "Alajuela",
      age = 68,
      birth_date = "12-05-1957",
      status = Status.SINGLE.value)
    
    Xinia = Person.create(
      name = "Xinia Carvajal Benavidez",
      cedula = "201220126",
      gender = "F",
      province = "Alajuela",
      age = 68,
      birth_date = "12-05-1957",
      status = Status.MARRIED.value)
    
    Rodolfo = Person.create(
      name = "Rodolfo Perez Sanchéz",
      cedula = "405120663",
      gender = "M",
      province = "Heredia",
      age = 75,
      birth_date = "23-03-1950",
      status = Status.MARRIED.value)
    
    Rodolfo = Person.create(
      name = "Rodolfo Perez Sanchéz",
      cedula = "405120663",
      gender = "M",
      province = "Heredia",
      age = 75,
      birth_date = "23-03-1950",
      status = Status.MARRIED.value)
    
    Jorge = Person.create(
      name = "Jorge Perez Carvajal",
      cedula = "208220543",
      gender = "M",
      province = "Alajuela",
      age = 22,
      birth_date = "25-01-2003",
      status = Status.MARRIED.value)
    
    Esteffany = Person.create(
      name = "Esteffany Brenes Arrieta",
      cedula = "108560346",
      gender = "F",
      province = "San José",
      age = 20,
      birth_date = "13-06-2005",
      status = Status.MARRIED.value)
    
    Amanda = Person.create(
      name = "Amanda Perez Brenes",
      cedula = "212350265",
      gender = "F",
      province = "Alajuela",
      age = 5,
      birth_date = "07-01-2020",
      status = Status.SINGLE.value)
    
    Fabriela = Person.create(
      name = "Fabriela Herrera Carvajal",
      cedula = "205640213",
      gender = "F",
      province = "Alajuela",
      age = 37,
      birth_date = "18-06-1988",
      status = Status.MARRIED.value)
    
    Anthony = Person.create(
      name = "Anthony Brenes Arrieta",
      cedula = "206390796",
      gender = "M",
      province = "Alajuela",
      age = 44,
      birth_date = "13-09-1981",
      status = Status.MARRIED.value)
    
    Gerald = Person.create(
      name = "Gerald Rojas Herrera",
      cedula = "215660213",
      gender = "M",
      province = "Alajuela",
      age = 44,
      birth_date = "13-04-2015",
      status = Status.MARRIED.value)
    
    Jordan = Person.create(
      name = "Jordan Herrera Carvajal",
      cedula = "208670191",
      gender = "M",
      province = "Alajuela",
      age = 20,
      birth_date = "12-06-2005",
      status = Status.SINGLE.value)
    

    

    

    
    

    

    
    
    
    
    
    



