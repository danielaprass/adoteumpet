from adoteumpet import database, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    nome_usuario = database.Column(database.String, nullable = False)
    senha = database.Column(database.String, nullable = False)
    email = database.Column(database.String, nullable = False, unique = True)
    nome = database.Column(database.String, nullable = True)
    foto = database.Column(database.String, default = 'default.png')
    data_criacao = database.Column(database.DateTime, nullable = False, default = datetime.utcnow())
    pets = database.relationship('Pet', backref = 'usuario', lazy = True)
    fotos_pets = database.relationship('FotoPet', backref = 'usuario', lazy = True)

class Pet(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    nome = database.Column(database.String, nullable = False)
    especie = database.Column(database.String, nullable = False)
    raca = database.Column(database.String, nullable = False)
    idade = database.Column(database.Integer, nullable = True)
    sexo = database.Column(database.String, nullable = False)
    peso = database.Column(database.Float, nullable = True)
    descricao = database.Column(database.String, nullable = True)
    disponivel = database.Column(database.Boolean, nullable = False, default = True)
    data_adocao = database.Column(database.DateTime, nullable = True)
    foto_pet = database.Column(database.String, default = 'default.png')
    data_criacao = database.Column(database.DateTime, nullable = False, default = datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable = False)


class FotoPet(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)


class FotoUsuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
