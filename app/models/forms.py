from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])
    relembre_me = BooleanField("relembre_me")

class SetorForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])

class UsuarioForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired()])
    setor = StringField("setor", validators=[DataRequired()])
    tipo = StringField("tipo", validators=[DataRequired()])

class ProdutoForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    catmat = StringField("catmat", validators=[DataRequired()])

class FornecedorForm(FlaskForm):
    razao_social = StringField("razao_social", validators=[DataRequired()])
    nome_fantasia = StringField("nome_fantasia", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    cnpj = StringField("cnpj", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])