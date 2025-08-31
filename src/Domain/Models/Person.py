from Database.Core.Peewee import db
from peewee import Model, AutoField, CharField, ForeignKeyField, IntegerField, DateField

GENDER_CHOICES = [("M", "Male"), ("F", "Female")]
STATUS_CHOICES = [("S", "Single"), ("M", "Married"), ("W", "Widowed"), ("D", "Deathed")]

class Person(Model):
  id = AutoField(primary_key=True)
  name = CharField(unique=True, max_length=100)
  cedula = CharField(unique=True, max_length=100)
  gender = CharField(max_length=1, choices=GENDER_CHOICES)

  province = CharField(max_length=100)
  emotional = IntegerField(default=100)

  age = IntegerField()
  birthdate = DateField()
  deathdate = DateField(null=True)
  status = CharField(max_length=1, choices=STATUS_CHOICES, default="S")

  guard = ForeignKeyField("self", backref="children", null=True, on_delete="SET NULL")
  mother = ForeignKeyField("self", backref="children_of_mother", null=True, on_delete="SET NULL")
  father = ForeignKeyField("self", backref="children_of_father", null=True, on_delete="SET NULL")

  class Meta:
    database = db
    table_name = "People"
