from Database.Peewee import db
from Models.Family import Family
from peewee import Model, AutoField, CharField, ForeignKeyField, IntegerField, DateField

class Person(Model):
  id = AutoField(primary_key=True)
  name = CharField(unique=True, max_length=100)
  cedula = CharField(unique=True, max_length=100)
  gender = CharField(max_length=10, choices=[("M", "Male"), ("F", "Female")])
  province = CharField(max_length=100)
  emotional = IntegerField(default=100)
  
  age = IntegerField()
  birthdate = DateField()
  deathdate = DateField(null=True)

  guard = ForeignKeyField("self", backref="children", null=True, on_delete="SET NULL")
  mother = ForeignKeyField("self", backref="children_of_mother", null=True, on_delete="SET NULL")
  father = ForeignKeyField("self", backref="children_of_father", null=True, on_delete="SET NULL")

  paternal_family = ForeignKeyField(Family, backref="paternal_members", null=True, on_delete="SET NULL")
  maternal_family = ForeignKeyField(Family, backref="maternal_members", null=True, on_delete="SET NULL")

  class Meta:
    database = db
    table_name = "Person"
