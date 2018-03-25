import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')


SQLALCHEMY_TRACK_MODIFICATIONS = True

#key for encript informations of formularies
SECRET_KEY = 'chavequalquer'


#SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/storage2.db'
# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'jay'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'jay'
#app.config['MYSQL_DATABASE_DB'] = 'BucketList'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'