from database.db import db

class Perro(db.Model):
    __tablename__ = 'Perros'
    ID = db.Column(db.Integer, primary_key=True)#    integer NOT NULL,
    Nombre = db.Column(db.String(50), nullable=False)#character varying(50) NOT NULL,
    Raza = db.Column(db.String(50), nullable=True)#character varying(50),
    Edad = db.Column(db.Integer, nullable=True)#integer,
    Peso = db.Column(db.Numeric(5, 2), nullable=True)#numeric(5, 2),
    ID_Cuidador = db.Column(db.Integer, db.ForeignKey('Cuidadores.ID'),  nullable=True)
    ID_Guarderia = db.Column(db.Integer,  nullable=True)

    #Create of the CRUD
    def crear_nuevo(id_perro, nombre, raza, edad, peso, id_cuidador):
        perro = Perro()
        perro.ID = id_perro
        perro.Nombre = nombre
        perro.Raza = raza
        perro.Edad = edad
        perro.Peso = peso
        perro.ID_Cuidador = id_cuidador
        perro.ID_Guarderia = 1

        db.session.add(perro)
        db.session.commit()

    #Read of the CRUD
    def traer_todos():
        return db.session.scalars(db.select(Perro).order_by(Perro.ID)).all()
    
    def consultar_por_nombre(nombre):
        #return db.session.execute(db.select(Perro).filter_by(Nombre=nombre)).scalars()
        return db.session.execute(\
                                  db.select(Perro)\
                                  .where(Perro.Nombre==nombre)\
                                  ).scalars()

    def consultar_por_id(id_perro):
        perro = db.get_or_404(Perro, id_perro)
        return perro

    #Update of the CRUD
    def modificar(id_perro, nombre, raza, edad, peso, id_cuidador):
        perro = db.get_or_404(Perro, id_perro)
        perro.Nombre = nombre
        perro.Raza = raza
        perro.Edad = edad
        perro.Peso = peso
        perro.ID_Cuidador = id_cuidador

        perro.verified = True

        db.session.commit()       

    def actualizar_cuidador(new_id_cuidador):
        db.session.execute(db.update(Perro)\
                                    .where(Perro.Peso <= 3)\
                                    .values(ID_Cuidador = new_id_cuidador))
        db.session.commit()
        return 

    #Delete of the CRUD
    def eliminar_por_id(id_perro):
        perro = db.get_or_404(Perro, id_perro)
        db.session.delete(perro)
        db.session.commit()
        return 
    

 

