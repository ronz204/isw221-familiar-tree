from Database.Peewee import db
from Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField, TimestampField, IntegerField

class Relation(Model):
  id = AutoField(primary_key=True)
  year = IntegerField()
  man = ForeignKeyField(Person, backref="relations_as_man", on_delete="CASCADE")
  woman = ForeignKeyField(Person, backref="relations_as_woman", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Relation"
