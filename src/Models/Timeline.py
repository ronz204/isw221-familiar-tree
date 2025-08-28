import datetime as dt
from Database.Peewee import db
from Models.Event import Event
from Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField, IntegerField, TimestampField

class Timeline(Model):
  id = AutoField(primary_key=True)
  year = IntegerField()
  event = ForeignKeyField(Event, backref="timelines", on_delete="CASCADE")
  person = ForeignKeyField(Person, backref="timelines", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Timeline"
