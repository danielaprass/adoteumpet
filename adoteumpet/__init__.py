from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///adoteumpet.db'
app.config['SECRET_KEY'] = '72b47d67d10a8566a79c94c1099ccda0'
app.config['UPLOAD_FOLDER_PETS'] = 'static/fotos_pets'
app.config['UPLOAD_FOLDER_USUARIOS'] = 'static/fotos_usuarios'

database = SQLAlchemy(app)

bcrypt= Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

from adoteumpet import routes