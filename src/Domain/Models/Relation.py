from Database.Core.Peewee import db
from Domain.Models.Person import Person
from peewee import Model, AutoField, ForeignKeyField, TimestampField, CharField

STATUS_CHOICES = [("C", "Current"), ("P", "Previous")]

class Relation(Model):
  id = AutoField(primary_key=True)
  timestamp = TimestampField()
  
  status = CharField(max_length=20, choices=STATUS_CHOICES, default="C")
  man = ForeignKeyField(Person, backref="relations_as_man", on_delete="CASCADE")
  woman = ForeignKeyField(Person, backref="relations_as_woman", on_delete="CASCADE")

  class Meta:
    database = db
    table_name = "Relation"
