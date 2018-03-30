from flask import Flask, render_template, url_for, request
from flask import redirect, url_for, session, flash, session
from app import app, db
from app.models.forms import LoginForm, ProdutoForm, UsuarioForm, SetorForm, FornecedorForm
#para o login
from app.models.tables import Usuario


#from app.models.tables import Setor
#from app.models.tables import Usuario

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
    return render_template('login.html', form_login=form_login)



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