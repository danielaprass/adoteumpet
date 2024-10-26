from flask import render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user

from adoteumpet import app, database, bcrypt
from adoteumpet.models import Usuario, Pet, FotoPet
from adoteumpet.forms import FormLogin, FormCriarConta, FormFotoPet

import os
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET', 'POST'])
def homepage():

    form_login = FormLogin()

    if form_login.validate_on_submit():

        usuario = Usuario.query.filter_by(email = form_login.email.data).first()

        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil_usuario', id_usuario = usuario.id))

    return render_template('homepage.html', form = form_login)

@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():

    form_criarconta  = FormCriarConta()

    if form_criarconta.validate_on_submit():

        usuario = Usuario(
            nome_usuario = form_criarconta.nome_usuario.data,
            senha = bcrypt.generate_password_hash(form_criarconta.senha.data),
            email = form_criarconta.email.data,
            nome = form_criarconta.nome.data,
            foto = form_criarconta.foto.data
        )

        database.session.add(usuario)
        database.session.commit()

        login_user(usuario, remember = True)
        return redirect(url_for('perfil_usuario', id_usuario = usuario.id))

    return render_template('criarconta.html', form = form_criarconta)


@app.route('/perfil/<id_usuario>', methods=['GET','POST'])
@login_required
def perfil_usuario(id_usuario):

    if int(id_usuario) == int(current_user.id):

        form_foto_pet = FormFotoPet()

        if form_foto_pet.validate_on_submit():
            arquivo = form_foto_pet.foto_pet.data
            nome_seguro = secure_filename(arquivo.filename)

            caminho = os.path.join(
                os.path.abspath(os.path.dirname(__file__)),
                app.config['UPLOAD_FOLDER'],
                nome_seguro
            )
            arquivo.save(caminho)

            foto_pet = FotoPet(
                imagem = nome_seguro,
                id_usuario = id_usuario
            )

            database.session.add(foto_pet)
            database.session.commit()

        return render_template('perfil_usuario.html', usuario = current_user, form = form_foto_pet)
    
    else:
        usuario = Usuario.query.get(int(id_usuario))
        return render_template('perfil_usuario.html', usuario = usuario, form = None)


@app.route('/pet/<nome_pet>')
@login_required
def perfil_pet(nome_pet):
    return render_template('perfil_pet.html', nome_pet=nome_pet)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/feed')
@login_required
def feed():
    fotos_pets = FotoPet.query.order_by(FotoPet.data_criacao.desc()).all()
    return render_template("feed.html", fotos_pets=fotos_pets)