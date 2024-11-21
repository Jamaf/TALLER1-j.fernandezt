from flask import Flask
from flask import render_template
from dotenv import load_dotenv
import os

from database.db import db
from database.db import init_db

from controllers.perro_controller import perro_blueprint
from controllers.cuidador_controller import cuidador_blueprint

#Cargar las variables ocultas
load_dotenv()

app = Flask(__name__, template_folder="views")

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #Por buena practica

#leer la variable oculta
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_STRING_CONNECTION')

#Aqui configuro la app para el objeto db
db.init_app(app)
init_db(app)

app.register_blueprint(perro_blueprint)
app.register_blueprint(cuidador_blueprint)

@app.route('/') 
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)