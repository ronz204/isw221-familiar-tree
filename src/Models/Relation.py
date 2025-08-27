import datetime as dt
from Database.Peewee import db
from Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField, TimestampField

class Relation(Model):
  id = AutoField(primary_key=True)
  timestamp = TimestampField(default=dt.datetime.now)
  person1 = ForeignKeyField(Person, backref="relations_as_person1", on_delete="CASCADE")
  person2 = ForeignKeyField(Person, backref="relations_as_person2", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Relation"
