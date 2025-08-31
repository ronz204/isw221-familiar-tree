from Database.Core.Peewee import db
from peewee import Model, AutoField, CharField

class Event(Model):
  id = AutoField(primary_key=True)
  name = CharField(unique=True, max_length=100)
  label = CharField(max_length=100)

  class Meta:
    database = db
    table_name = "Event"
