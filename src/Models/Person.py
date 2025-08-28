from Database.Peewee import db
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

  guardian = ForeignKeyField("self", backref="children", null=True, on_delete="SET NULL")
  mother = ForeignKeyField("self", backref="children_of_mother", null=True, on_delete="SET NULL")
  father = ForeignKeyField("self", backref="children_of_father", null=True, on_delete="SET NULL")

  status = CharField(max_length=20, choices=[("S", "Single"), ("M", "Married"), ("W", "Widowed"), ("D", "Deathed")], default="S")

  class Meta:
    database = db
    table_name = "Person"
