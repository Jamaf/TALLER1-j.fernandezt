from flask import Flask, request, url_for
from flask import render_template, redirect
from flask_login import LoginManager, login_user, login_required, current_user
from dotenv import load_dotenv
import os

from database.db import db
from database.db import init_db

from controllers.perro_controller import perro_blueprint
from controllers.cuidador_controller import cuidador_blueprint

from models.usuario import Usuario

#Cargar las variables ocultas
load_dotenv()

app = Flask(__name__, template_folder="views")
login_manager = LoginManager(app)

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Por buena practica

SECRET_KEY = os.urandom(24)
app.config["SECRET_KEY"] = SECRET_KEY

#Aqui configuro la app para el objeto db
db.init_app(app)
init_db(app)

app.register_blueprint(perro_blueprint)
app.register_blueprint(cuidador_blueprint)

@login_manager.user_loader
def load_user(user_id):
    usuario = Usuario.consultar_por_id(int(user_id))

    return usuario


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]

        usuario = Usuario.consultar_por_nombre_password(username, password)
        
        if usuario is not None:
            login_user(usuario[0])
            if usuario[0].rol.Nombre == 'Administrador':
                return redirect(url_for('perro_bp.listar'))
            else:
                return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.rol.Nombre != 'Administrador':
        return render_template("dashboard.html", usuario = current_user)       
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)