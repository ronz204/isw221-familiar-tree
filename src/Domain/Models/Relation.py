from Models.Person import Person
from Database.Core.Peewee import db
from peewee import Model, AutoField, ForeignKeyField, TimestampField

class Relation(Model):
  id = AutoField(primary_key=True)
  timestamp = TimestampField()

  man = ForeignKeyField(Person, backref="relations_as_man", on_delete="CASCADE")
  woman = ForeignKeyField(Person, backref="relations_as_woman", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Relation"
