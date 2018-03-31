from flask import Flask, render_template, request
from flask import redirect, url_for, session, flash
from app import app, db, lm
from app.models.forms import LoginForm, ProdutoForm, UsuarioForm, SetorForm, FornecedorForm
#para o login
from flask_login import login_user, logout_user, login_required
from app.models.tables import Usuario

#from app.models.tables import Setor
#from app.models.tables import Usuario



@lm.user_loader
def load_user(id):
    return Usuario.query.filter_by(id=id).first()


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    produto_form = ProdutoForm()
    #flash("Bem Vindo ao SGPL")
    return render_template('index.html', produto_form = produto_form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = LoginForm()
    #Login-Manager
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and usuario.senha == form_login.senha.data:
            login_user(usuario, force=True, remember=True)
            flash("Logado!")
            return redirect(url_for("index"))
        else:
            flash("Login Inválido!")
            return redirect(url_for("login"))
    return render_template('login.html', form_login=form_login)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/cadastrar-setor")
@app.route("/cadastrar-usuario")
def cadastrar_usuario():
    form_usuario = UsuarioForm()
    form_setor = SetorForm()
    form_fornecedor = FornecedorForm()
    data = {}
    data[0] = form_usuario
    data[1] = form_setor
    data[2] = form_fornecedor
    return render_template('cadastrar/cadastrarUsuario.html', data=data)