# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from .models import *


#Instância do arquivo de configuração
app = Flask(__name__)
app.config.from_object('config')


#Instância do banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Instância do banco do arquivo de gerenciamento
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="0.0.0.0", port=9000))

#Instância da API
api = Api(app)

#Instância da Login-Manager
lm = LoginManager(app)
lm.init_app(app)

#Não esquecer dessa linha, sem ela as tabelas não são criadas com o migrate
from app import  views
from app.controllers import default_routes

