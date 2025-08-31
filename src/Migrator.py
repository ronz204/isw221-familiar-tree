from peewee import SqliteDatabase
from Database.Core.Peewee import db

from Domain.Models.Event import Event
from Domain.Models.Person import Person
from Domain.Models.Relation import Relation
from Domain.Models.Timeline import Timeline

class Migrator:
  def __init__(self, database: SqliteDatabase):
    self.database = database
    self.models = [Event, Person, Relation, Timeline]

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

migrator = Migrator(database=db)
migrator.migrate()
