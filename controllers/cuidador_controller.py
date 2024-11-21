from models.cuidador import Cuidador

from flask import jsonify
from flask import Blueprint
from flask import render_template, redirect, url_for, request
cuidador_blueprint = Blueprint('cuidador_bp', __name__, url_prefix="/cuidadores")

@cuidador_blueprint.route('/listar') 
def listar():
    return Cuidador.traer_todos()

#    for cuidador in todos_los_cuidadores:
#        print(cuidador.to_json())

   # return jsonify(todos_los_cuidadores[0].to_json())
@cuidador_blueprint.route('/listar_json') 
def listar_json():
    todos_los_cuidadores = Cuidador.traer_todos()   
    return jsonify(todos_los_cuidadores)