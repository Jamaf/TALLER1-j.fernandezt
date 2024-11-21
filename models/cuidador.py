from database.db import db
from dataclasses import dataclass

#Para volverla serializble
@dataclass
class Cuidador(db.Model):
    __tablename__ = 'Cuidadores'

    #Para que dataclass pueda armar el json
    ID: int
    Nombre: str
    Telefono: str

    ID = db.Column(db.Integer, primary_key=True)#    integer NOT NULL,
    Nombre = db.Column(db.String(50), nullable=False)#character varying(50) NOT NULL,
    Telefono = db.Column(db.String(50), nullable=True)#character varying(50),

    def traer_todos():
        return db.session.scalars(db.select(Cuidador).order_by(Cuidador.ID)).all()
    
    def to_json(self):
        return f'"ID": {self.ID}, "Nombre": {self.Nombre}, "Telefono": {self.Telefono}'