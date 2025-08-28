from Database.Peewee import db
from Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField, TimestampField, IntegerField

class Relation(Model):
  id = AutoField(primary_key=True)
  year = IntegerField()
  person1 = ForeignKeyField(Person, backref="relations_as_person1", on_delete="CASCADE")
  person2 = ForeignKeyField(Person, backref="relations_as_person2", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Relation"
