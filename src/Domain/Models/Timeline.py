from Models.Event import Event
from Models.Person import Person
from Database.Core.Peewee import db
from peewee import Model, AutoField, ForeignKeyField, TimestampField

class Timeline(Model):
  id = AutoField(primary_key=True)
  timestamp = TimestampField()

  event = ForeignKeyField(Event, backref="timelines", on_delete="CASCADE")
  person = ForeignKeyField(Person, backref="timelines", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Timeline"
