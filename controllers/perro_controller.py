from models.perro import Perro
from controllers import cuidador_controller

from flask import jsonify
from flask import Blueprint
from flask import render_template, redirect, url_for, request
perro_blueprint = Blueprint('perro_bp', __name__, url_prefix="/perros")


@perro_blueprint.route('/') 
def index():
    return render_template("perros/perro_index.html")

@perro_blueprint.route('/agregar_perro_form') 
def agregar_perro_form():
    cuidadores = cuidador_controller.listar()
    return render_template("perros/agregar.html", cuidadores = cuidadores)

#Método para "Create"
@perro_blueprint.route('/agregar_perro', methods=['POST']) 
def agregar_perro():
    
    #print(f"Agregar perro con Nombre : {request.form['nombre']}")    
    id_perro = request.form['id_perro']
    nombre = request.form['nombre']
    raza = request.form['raza']
    edad = request.form['edad']
    peso = request.form['peso']
    id_cuidador = request.form['id_cuidador']

    Perro.crear_nuevo(id_perro, nombre, raza, edad, peso, id_cuidador)

    return redirect(url_for('perro_bp.listar'))

#Métodos para "Read"
@perro_blueprint.route('/listado', methods=['GET']) 
def listar():
    todos_los_perros = Perro.traer_todos()
    return render_template("perros/listado.html", perros = todos_los_perros)

@perro_blueprint.route('/buscar/<string:nombre>/', methods=['GET']) 
def buscar(nombre:str):
    perros_filtrados = Perro.consultar_por_nombre(nombre)
    print(f'Buscando {nombre}')
    return render_template("perros/listado.html", perros = perros_filtrados)

#Métodos para "Update"
@perro_blueprint.route('/modificar_perro', methods = ['POST'])
def modificar_perro():
    id_perro = request.form['id_perro']
    nombre = request.form['nombre']
    raza = request.form['raza']
    edad = request.form['edad']
    peso = request.form['peso']
    id_cuidador = request.form['id_cuidador']

    Perro.modificar(id_perro, nombre, raza, edad, peso, id_cuidador)

    return redirect(url_for('perro_bp.listar'))


@perro_blueprint.route('/modificar_perro_form/<int:id>/') 
def modificar_perro_form(id:int):
    perro_filtrado = Perro.consultar_por_id(id)
    cuidadores = cuidador_controller.listar()
    #print(f'Modificar perro con ID: {id}')
    return render_template("perros/modificar_perro.html", perro = perro_filtrado, cuidadores = cuidadores)

@perro_blueprint.route('/actualizar_cuidador_mario') 
def actualizar_cuidador_mario():
    id_cuidador_mario = 1
    Perro.actualizar_cuidador(id_cuidador_mario)
    return redirect(url_for('perro_bp.listar'))

#Métodos para "Delete"
@perro_blueprint.route('/borrar_perro/<int:id>/') 
def borrar_perro(id:int):
    Perro.eliminar_por_id(id)
    #print(f'Eliminar perro con ID: {id}')    
    return redirect(url_for('perro_bp.listar'))

