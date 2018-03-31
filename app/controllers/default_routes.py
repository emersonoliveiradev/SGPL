from flask import Flask, render_template, request
from flask import redirect, url_for, session, flash
from app import app, db, lm
from app.models.forms import LoginForm, ProdutoForm, UsuarioForm, SetorForm, FornecedorForm
#para o login
from flask_login import login_user, logout_user, login_required
from app.models.tables import Usuario, Setor, Fornecedor

#from app.models.tables import Setor
#from app.models.tables import Usuario


@lm.user_loader
def load_user(id):
    return Usuario.query.filter_by(id=id).first()

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


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    produto_form = ProdutoForm()
    #flash("Bem Vindo ao SGPL")
    return render_template('index.html', produto_form = produto_form)



@app.route("/cadastrar-usuario", methods=["GET", "POST"])
def cadastrar_usuario():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        tipo = request.form.get("tipo")
        setor = request.form.get("setor")

        if nome and email and senha and tipo and setor:
            usuario = Usuario(nome, email, senha, tipo, setor)
            db.session.add(usuario)
            db.session.commit()
            flash("Cadastro de usuário realizado com sucesso!")
            return redirect(url_for('cadastrar_usuario'))

    form_usuario = UsuarioForm()
    form_setor = SetorForm()
    form_fornecedor = FornecedorForm()
    data = [form_usuario, form_setor, form_fornecedor]
    return render_template('cadastrar/cadastrarUsuario.html', data=data)



@app.route("/cadastrar-setor", methods=["GET", "POST"])
def cadastrar_setor():
    if request.method == "POST":
        nome = request.form.get("nome")

        if nome:
            setor = Setor(nome)
            db.session.add(setor)
            db.session.commit()
            flash("Cadastro de setor realizado com sucesso!")
            return redirect(url_for('cadastrar_usuario'))

    return render_template('cadastrar/cadastrarUsuario.html')


@app.route("/cadastrar-fornecedor", methods=["GET", "POST"])
def cadastrar_fornecedor():
    if request.method == "POST":
        razao_social = request.form.get("razao_social")
        nome_fantasia = request.form.get("nome_fantasia")
        email = request.form.get("email")
        cnpj = request.form.get("cnpj")
        telefone = request.form.get("telefone")

        if razao_social and nome_fantasia and email and cnpj and telefone:
            fornecedor = Fornecedor(razao_social, nome_fantasia, email, cnpj, telefone)
            db.session.add(fornecedor)
            db.session.commit()
            flash("Cadastro de fornecedor realizado com sucesso!")
            return redirect(url_for('cadastrar_usuario'))

    return render_template('cadastrar/cadastrarUsuario.html')