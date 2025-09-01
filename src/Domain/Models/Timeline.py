from Database.Core.Peewee import db
from Domain.Models.Event import Event
from Domain.Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField, DateField

class Timeline(Model):
  id = AutoField(primary_key=True)
  timestamp = DateField()

  event = ForeignKeyField(Event, backref="timelines", on_delete="CASCADE")
  person = ForeignKeyField(Person, backref="timelines", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Timeline"
