from app import db



from sqlalchemy import Column, Integer, String
from database_settings import Base
import database_settings

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
    tipo2 = db.Column(db.Integer)

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
