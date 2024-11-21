from database.db import db

class Usuario(db.Model):
    __tablename__ = 'Usuarios'
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    ID_Rol = db.Column(db.Integer, db.ForeignKey('Roles.ID'),  nullable=False)