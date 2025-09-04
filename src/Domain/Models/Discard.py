from Database.Core.Peewee import db
from Domain.Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField

class Discard(Model):
  id = AutoField(primary_key=True)
  man = ForeignKeyField(Person, backref="relations_as_man", on_delete="CASCADE")
  woman = ForeignKeyField(Person, backref="relations_as_woman", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Discard"
