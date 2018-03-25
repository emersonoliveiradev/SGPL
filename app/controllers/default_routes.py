from flask import Flask, render_template, url_for, request
from flask import redirect, url_for, session, flash, session
from app import app, db
from app.models.forms import LoginForm, ProdutoForm
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


@app.route("/logger", methods=['POST'])
def logger1():
    error = None
    usuario = db.session.query(Usuario).filter_by(nome=request.form['nome']).first()
    if request.method == 'POST':
        if not usuario:
            error = 'Credencial Invalida!'
        else:
            print(request.form['nome'])
            return redirect(url_for('index'))

    return render_template('index.html', error=error)

'''
def logger2():
@app.route("/logger/nome", methods=['GET'])
    usuario = db.session.query(Usuario).filter_by(nome=request.form['nome']).first()
    if request.method == 'GET':
        if not usuario:
            error = 'Credencial Invalida!'
        else:
            print(request.form['nome'])
            return redirect(url_for('index'))

    return render_template('index.html', error=error)
'''


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    flash("Voce precisa estar logado!")
    #session.pop['logged_in', None]
    return redirect(url_for('login'))