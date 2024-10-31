from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from adoteumpet.models import Usuario

class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Fazer login')


class FormCriarConta(FlaskForm):
    nome = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    foto = FileField('Foto de Perfil')
    botao_confirmacao = SubmitField('Criar conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email = email.data).first()
        if usuario:
            return ValidationError('E-mail já cadastrado, faça login para continuar')
        

class FormAdicionarPet(FlaskForm):
    nome = StringField('Nome')
    especie = StringField('Espécie')
    raca = StringField('Espécie')
    idade = IntegerField('Idade')
    sexo = StringField('Sexo')
    peso = DecimalField('Peso')
    descricao = StringField('Descrição')
    foto_pet = FileField('Foto do Pet', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Enviar')