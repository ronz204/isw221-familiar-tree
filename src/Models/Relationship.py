from Database.Peewee import db
from Models.Person import Person
from peewee import Model, AutoField, CharField, ForeignKeyField, Check

RELATIONSHIP_TYPES = [
  ("parent", "Parent"),
  ("child", "Child"),
  ("grandparent", "Grandparent"),
  ("grandchild", "Grandchild"),
  ("sibling", "Sibling"),
  ("spouse", "Spouse"),
  ("great_grandparent", "Great Grandparent"),
  ("great_grandchild", "Great Grandchild"),
  ("aunt_uncle", "Aunt/Uncle"),
  ("nephew_niece", "Nephew/Niece"),
  ("cousin", "Cousin"),
]

class Relationship(Model):
  id = AutoField(primary_key=True)
  person1 = ForeignKeyField(Person, backref="relationships", on_delete="CASCADE")
  person2 = ForeignKeyField(Person, backref="reverse_relationships", on_delete="CASCADE")
  type = CharField(max_length=50, choices=RELATIONSHIP_TYPES)

  class Meta:
    database = db
    table_name = "Relationship"
    constraints = [Check("person1_id != person2_id")]
