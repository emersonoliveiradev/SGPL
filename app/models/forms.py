from flask_wtf import FlaskForm
import datetime
from sqlalchemy import DateTime, Date, desc
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models.tables import Usuario, Fornecedor, Pedido, Produto

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
    data = StringField(Date, default=datetime.date.today())
    usuario = QuerySelectField('Usuario', query_factory=lambda: Usuario.query.filter_by(tipo="1"),
                               get_label='nome', allow_blank=True,
                               blank_text=(u'Selecione um usuário'), get_pk=lambda x: x.id)
    requisitante = QuerySelectField('Usuario', query_factory=lambda: Usuario.query.filter_by(tipo="2"),
                               get_label='nome', allow_blank=True,
                               blank_text=('Selecione um requisitante'), get_pk=lambda x: x.id)
    #Item_do_Pedido
    quantidade = StringField("quantidade", validators=[DataRequired()])
    fornecedor1 = QuerySelectField('fornecedor', query_factory=lambda: Fornecedor.query.all(),
                               get_label='nome_fantasia', allow_blank=True,
                               blank_text=('Selecione um fornecedor (1)'), get_pk=lambda x: x.id)
    fornecedor2 = QuerySelectField('fornecedor', query_factory=lambda: Fornecedor.query.all(),
                                   get_label='nome_fantasia', allow_blank=True,
                                   blank_text=('Selecione um fornecedor (2)'), get_pk=lambda x: x.id)
    fornecedor3 = QuerySelectField('fornecedor', query_factory=lambda: Fornecedor.query.all(),
                                   get_label='nome_fantasia', allow_blank=True,
                                   blank_text=('Selecione um fornecedor (3)'), get_pk=lambda x: x.id)
    valor_fornecedor1 = StringField("valor_fornecedor1", validators=[DataRequired()])
    valor_fornecedor2 = StringField("valor_fornecedor2", validators=[DataRequired()])
    valor_fornecedor3 = StringField("valor_fornecedor3", validators=[DataRequired()])
    produto = QuerySelectField('produto', query_factory=lambda: Produto.query.all(),
                                   get_label='nome', allow_blank=True,
                                   blank_text=('Selecione um poduto'), get_pk=lambda x: x.id)
    enviar = SubmitField("Enviar")




class PregaoForm(FlaskForm):
    quantidade = StringField("quantidade", validators=[DataRequired()])
    fornecedor = QuerySelectField('Fornecedor', query_factory=lambda: Fornecedor.query.all(),
                                   get_label='nome_fantasia', allow_blank=True,
                                   blank_text=('Selecione um fornecedor (1)'), get_pk=lambda x: x.id)
    valor_referencia = StringField("valor_referencia", validators=[DataRequired()])
    pedido = QuerySelectField('Pedido', query_factory=lambda: Pedido.query.all(),
                              get_label='id', allow_blank=True,
                              blank_text=('Selecione um pedido'), get_pk=lambda x: 'id')
    produto = QuerySelectField('Produto', query_factory=lambda: Produto.query.all(),
                               get_label='nome', allow_blank=True,
                               blank_text=('Selecione um poduto'), get_pk=lambda x: 'id')
    enviar = SubmitField("Enviar")
