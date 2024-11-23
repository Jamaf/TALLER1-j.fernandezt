from models.perro import Perro
from controllers import cuidador_controller

from flask import jsonify
from flask import Blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
perro_blueprint = Blueprint('perro_bp', __name__, url_prefix="/perros")


#Métodos para "Read"
@perro_blueprint.route('/listado', methods=['GET']) 
@login_required
def listar():
    if current_user.rol.Nombre == 'Administrador':
        todos_los_perros = Perro.traer_todos()
        return render_template("perros/listado.html", perros = todos_los_perros)    
    else:
        return redirect(url_for('login'))    

#Métodos para "Update"
@perro_blueprint.route('/modificar_perro', methods = ['POST'])
@login_required
def modificar_perro():
    if current_user.rol.Nombre == 'Administrador':        
        id_perro = request.form['id_perro']
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        peso = request.form['peso']
        id_cuidador = request.form['id_cuidador']

        Perro.modificar(id_perro, nombre, raza, edad, peso, id_cuidador)

        return redirect(url_for('perro_bp.listar'))
    else:
        return redirect(url_for('login'))    

@perro_blueprint.route('/modificar_perro_form/<int:id>/') 
@login_required
def modificar_perro_form(id:int):
    if current_user.rol.Nombre == 'Administrador':    
        perro_filtrado = Perro.consultar_por_id(id)
        cuidadores = cuidador_controller.listar()
        #print(f'Modificar perro con ID: {id}')
        return render_template("perros/modificar_perro.html", perro = perro_filtrado, cuidadores = cuidadores)
    else:
        return redirect(url_for('login')) 

#Métodos para "Delete"
@perro_blueprint.route('/borrar_perro/<int:id>/') 
@login_required
def borrar_perro(id:int):
    if current_user.rol.Nombre == 'Administrador':    
        Perro.eliminar_por_id(id)
        #print(f'Eliminar perro con ID: {id}')    
        return redirect(url_for('perro_bp.listar'))
    else:
        return redirect(url_for('login'))   


@perro_blueprint.route('/buscar/<string:nombre>/', methods=['GET']) 
@login_required
def buscar(nombre:str):
    if current_user.rol.Nombre == 'Administrador':    
        perros_filtrados = Perro.consultar_por_nombre(nombre)
        print(f'Buscando {nombre}')
        return render_template("perros/listado.html", perros = perros_filtrados)
    else:
        return redirect(url_for('login'))    
    

@perro_blueprint.route('/agregar_perro_form') 
@login_required
def agregar_perro_form():
    if current_user.rol.Nombre == 'Administrador':    
        cuidadores = cuidador_controller.listar()
        return render_template("perros/agregar.html", cuidadores = cuidadores)
    else:
        return redirect(url_for('login'))   
    
#Método para "Create"
@perro_blueprint.route('/agregar_perro', methods=['POST']) 
@login_required
def agregar_perro():
    if current_user.rol.Nombre == 'Administrador':    
        #print(f"Agregar perro con Nombre : {request.form['nombre']}")    
        id_perro = request.form['id_perro']
        nombre = request.form['nombre']
        raza = request.form['raza']
        edad = request.form['edad']
        peso = request.form['peso']
        id_cuidador = request.form['id_cuidador']

        Perro.crear_nuevo(id_perro, nombre, raza, edad, peso, id_cuidador)

        return redirect(url_for('perro_bp.listar'))
    else:
        return redirect(url_for('login'))   