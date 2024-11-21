from database.db import db

class Guarderia(db.Model):
    #__table__ = db.metadata.tables["Guarderias"]
    __table__ = db.Table('Guarderias', db.metadata, autoload = True, autoload_with=db.engine)