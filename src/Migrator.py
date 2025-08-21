from Database.Peewee import db
from Models.Family import Family
from Models.Person import Person
from peewee import SqliteDatabase

class Migrator:
  def __init__(self, database: SqliteDatabase):
    self.db = database
    self.models = [Family, Person]

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

migrator = Migrator(db)
migrator.migrate() 