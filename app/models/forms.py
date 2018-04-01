from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models.tables import Usuario

class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    senha = StringField("senha", validators=[DataRequired()])
    relembre_me = BooleanField("relembre_me")
    enviar = SubmitField("Enviar")


class SetorForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    enviar = SubmitField("Enviar")


class UsuarioForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    senha = PasswordField("senha", validators=[DataRequired()])
    setor = StringField("setor", validators=[DataRequired()])
    tipo = StringField("tipo", validators=[DataRequired()])
    enviar = SubmitField("Enviar")

class ProdutoForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    catmat = StringField("catmat", validators=[DataRequired()])
    enviar = SubmitField("Enviar")


class FornecedorForm(FlaskForm):
    razao_social = StringField("razao_social", validators=[DataRequired()])
    nome_fantasia = StringField("nome_fantasia", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    cnpj = StringField("cnpj", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])
    enviar = SubmitField("Enviar")


#https://stackoverflow.com/questions/49025345/flask-wtforms-queryselectfield-to-set-form-select-option-values
class PedidoForm(FlaskForm):
    usuario = QuerySelectField('Usuario', query_factory=lambda: Usuario.query.all(), get_label='nome',
                               allow_blank=True, blank_text=(u'Selecione um usuário'), get_pk=lambda x: 'id')

    enviar = SubmitField("Enviar")


