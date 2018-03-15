from app import db
# from app import Schema
# from app import Schema
from flask import Flask, request, jsonify
import requests as req

#Setor
class Setor(db.Model):
    __tablename__ = "setores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def __init__(self, nome):
        self.nome = nome

    # Return informations about User
    def __repr__(self):
        return "<Setor %r>" % self.nome

#Usuario
class Usuario(db.Model):
    #Create table
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(50))
    setor = db.Column(db.Integer, db.ForeignKey('setores.id'))
    tipo = db.Column(db.Integer)

    #setor = db.relationship('Setor', foreign_keys=setor.id)

    #Set required / initialize an user
    def __init__(self, nome, email, senha, setor, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.setor = setor
        self.tipo = tipo

        # Return informations about User
        def __repr__(self):
            return "<usuario %r>" % self.nome

#Fornecedor
class Fornecedor(db.Model):
    #Create table
    __tablename__ = "fornecedores"

    id = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(50))
    nome_fantasia = db.Column(db.String(50))
    email = db.Column(db.String(50))
    cnpj = db.Column(db.String(11))
    telefone = db.Column(db.String(20))

    #Set required / initialize a
    def __init__(self, razao_social, nome_fantasia, email, cnpj, telefone):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.email = email
        self.cnpj = cnpj
        self.telefone = telefone

        # Return informations about User
        def __repr__(self):
            return "<fornecedor %r>" % self.nome_fantasia

#Pedido
class Pedido(db.Model):
    __tablename__ = "pedidos"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50))
    requisitante = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    itens = db.Column(db.Integer, db.ForeignKey('itens_do_pedido.id')) #Criar tabela itens
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __init__(self, data, itens, requisitante, usaurio):
        self.data = data
        self.itens = itens
        self.requisitante = requisitante
        self.usuario = usuario

    # Return informations about User
    def __repr__(self):
        return "<Setor %r>" % self.data

#Produto
class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    catmat = db.Column(db.String(50))   #Ver tamanho catmat

    def __init__(self, nome, catmat):
        self.nome = nome
        self.catmat = catmat

    # Return informations about User
    def __repr__(self):
        return "<Produto %r>" % self.nome


#Item do pedido
class Item_do_Pedido(db.Model):
    #Create table
    __tablename__ = "itens_do_pedido"

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)
    fornecedor_1 = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    fornecedor_2 = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    fornecedor_3 = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    valor_fornecedor_1 = db.Column(db.Numeric(12, 2))
    valor_fornecedor_2 = db.Column(db.Numeric(12, 2))
    valor_fornecedor_3 = db.Column(db.Numeric(12, 2))
    pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    produto = db.Column(db.Integer, db.ForeignKey('produtos.id'))

    def __init__(self, quantidade, fornecedor_1, fornecedor_2, fornecedor_3, valor_fornecedor_1, valor_fornecedor_2, valor_fornecedor_3, pedido, produto):
        self.quantidade = quantidade
        self.fornecedor_1 = fornecedor_1
        self.fornecedor_2 = fornecedor_2
        self.fornecedor_3 = fornecedor_3
        self.valor_fornecedor_1 = valor_fornecedor_2
        self.valor_fornecedor_2 = valor_fornecedor_2
        self.valor_fornecedor_3 = valor_fornecedor_3
        self.pedido = pedido
        self.produto = produto


#Pedido tem Item do Pedido
class Pedido_tem_Item_do_Pedido(db.Model):
    #Create table
    __tablename__ = "pedido_tem_item_do_pedido"

    id = db.Column(db.Integer, primary_key=True)
    pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    item_do_pedido = db.Column(db.Integer, db.ForeignKey('itens_do_pedido.id'))
    status = db.Column(db.Integer)

    def __init__(self, pedido, item_do_pedido, status):
        self.pedido = pedido
        self.item_do_pedido = item_do_pedido
        self.status = status


#Fornecedor
class Fornecedor_fornece_Produto(db.Model):
    #Create table
    __tablename__ = "fornecedor_fornece_produto"

    id = db.Column(db.Integer, primary_key=True) #RETIRAR ISSO
    fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    produto = db.Column(db.Integer, db.ForeignKey('produtos.id'))


#Pregao
class Pregao(db.Model):
    #Create table
    __tablename__ = "pregoes"

    id = db.Column(db.Integer, primary_key=True)
    pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    requisitante = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    #item_do_pregao = db.Column(db.Integer, db.ForeignKey('itens_do_pregao.id'))

    def __init__(self, pedido, requisitante, usuario, item_do_pregao):
        self.pedido = pedido
        self.requisitante = requisitante
        self.usuario = usuario
        #self.item_do_pregao = item_do_pregao

