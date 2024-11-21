from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy(app)
#Lo vamos a inciair sin app
#luego en el app.py se le configura
db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        db.create_all()
