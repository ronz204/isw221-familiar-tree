from Database.Peewee import db
from Models.Family import Family
from peewee import Model, AutoField, CharField, ForeignKeyField, IntegerField, DateField

#, choices=[("M", "Male"), ("F", "Female")]

class Person(Model):
  id = AutoField(primary_key=True)
  name = CharField(unique=True, max_length=100)
  cedula = CharField(unique=True, max_length=100)
  gender = CharField(max_length=10, choices=[("M", "Male"), ("F", "Female")])
  province = CharField(max_length=100)
  emotional = IntegerField(default=100)
  birthdate = DateField()
  deathdate = DateField(null=True)
  couple = ForeignKeyField("self", backref="partners", null=True, on_delete="SET NULL")
  family = ForeignKeyField(Family, backref="members", null=True, on_delete="SET NULL")

  class Meta:
    database = db
    table_name = "Person"
