from Database.Peewee import db
from Database.Migrator import Migrator

migrator = Migrator(db)
migrator.migrate()
