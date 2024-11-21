from database.db import db

class Usuario(db.Model):
    __tablename__ = 'Roles'
    ID = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(50), nullable=False)