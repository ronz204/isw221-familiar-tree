from typing import List
from peewee import SqliteDatabase
from Database.Core.Peewee import db
from Database.Core.Seeder import Seeder

from Domain.Models.Event import Event
from Domain.Models.Person import Person
from Domain.Models.Discard import Discard
from Domain.Models.Affinity import Affinity
from Domain.Models.Passions import Passions
from Domain.Models.Relation import Relation
from Domain.Models.Timeline import Timeline

from Database.Seeders.EventSeeder import EventSeeder
from Database.Seeders.AffinitySeeder import AffinitySeeder

class Migrator:
  def __init__(self, database: SqliteDatabase):
    self.database = database
    self.models = [Event, Person, Discard, Relation, Timeline, Affinity, Passions]

  def migrate(self) -> None:
    try:
      self.database.connect()
      self.database.create_tables(self.models)
      print("Migration successful.")
    except Exception as e:
      print(f"Migration failed: {e}")
    finally:
      if not self.database.is_closed():
        self.database.close()

  def seeding(self) -> None:
    seeders: List[Seeder] = [
      EventSeeder,
      AffinitySeeder,
    ]

    for seeder in seeders:
      seeder().seed()


migrator = Migrator(database=db)
migrator.migrate()
migrator.seeding()
