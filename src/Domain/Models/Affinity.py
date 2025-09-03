from Database.Core.Peewee import db
from peewee import Model, AutoField, CharField

class Affinity(Model):
  id = AutoField(primary_key=True)
  name = CharField(unique=True, max_length=100)

  class Meta:
    database = db
    table_name = "Affinity"
