from flask import Flask
from flask_restful import Api

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from flask.ext.mysql import MySQL
#from marshmallow import Schema

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host="0.0.0.0", port=9000))

mysql = MySQL()
mysql.init_app(app)


#Não esquecer dessa linha, sem ela as tabelas não são criadas com o migrate
from app import  views
#from app.models import Setor
#from app.models import Usuario
from app.models.tables import Setor, Usuario
from app.models import forms
from app.controllers import default_routes