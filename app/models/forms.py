from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    #poralidators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class SetorForm(FlaskForm):
    nomeSetor = StringField("nomeSetor", validators=[DataRequired()])

class UsuarioForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired()])
    setor = StringField("setor", validators=[DataRequired()])

class ProdutoForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    catmat = StringField("catmat", validators=[DataRequired()])

class FornecedorForm(FlaskForm):
    razaoSocial = StringField("razaoSocial", validators=[DataRequired()])
    nomeFantasia = StringField("nomeFantasia", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    cnpj = StringField("cnpj", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])