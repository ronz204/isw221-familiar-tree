from typing import List
from Database.Peewee import db
from peewee import SqliteDatabase
from Database.Seeder import Seeder

from Models.Event import Event
from Models.Family import Family
from Models.Person import Person
from Models.Timeline import Timeline
from Models.Relation import Relation

from Database.Seeders.EventSeeder import EventSeeder

SEEDERS: List[Seeder] = [
  EventSeeder,
]

class Migrator:
  def __init__(self, database: SqliteDatabase):
    self.db = database
    self.models = [Event, Family, Person, Timeline, Relation]

  def migrate(self) -> None:
    try:
      self.db.connect()
      self.db.create_tables(self.models)
      print("Tablas creadas correctamente (si no existían).")
    except Exception as e:
      print(f"Error al crear tablas: {e}")
    finally:
      if not self.db.is_closed():
        self.db.close()
  
  def seeding(self) -> None:
    for seeder in SEEDERS:
      seeder().seed()

migrator = Migrator(db)

migrator.migrate()
migrator.seeding()
