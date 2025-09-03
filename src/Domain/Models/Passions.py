from Database.Core.Peewee import db
from Domain.Models.Person import Person
from Domain.Models.Affinity import Affinity
from peewee import Model, AutoField, ForeignKeyField

class Passions(Model):
  id = AutoField(primary_key=True)
  user = ForeignKeyField(Person, backref="passions")
  affinity = ForeignKeyField(Affinity, backref="passions")

  class Meta:
    database = db
    table_name = "Passions"
