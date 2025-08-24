import datetime as dt
from Database.Peewee import db
from Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField, CharField, DateTimeField

class Timeline(Model):
  id = AutoField(primary_key=True)
  event = CharField(max_length=255)
  timestamp = DateTimeField(default=dt.datetime.now)
  person = ForeignKeyField(Person, backref="timelines", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Timeline"
