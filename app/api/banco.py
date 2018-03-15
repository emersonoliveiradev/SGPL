from flask import Flask
import peewee #Database ORM
from flask import Flask, jsonify, request #Helper JSON #"Helper requisition"

app = Flask(__name__)
banco = peewee.SqliteDatabase('../storage.db')

#class Postagem(peewee.Model):
#    titulo = peewee.CharField()
#   conteudo = peewee.TextField()
#
#   def to_dict(self):
#       return {'id':self.id, 'titulo': self.titulo, 'conteudo': self.conteudo}
#
#   class Meta:
#       database = banco


def initialize_db():
    banco.connect()
    #banco.create_tables([Usuario], safe = True)
    banco.close()


@app.route('/usuarios/<int:id_usuario>')
def usuario(id_usuario):
    try:
        usuario = Usuario.get(id=id_usuario)
        return jsonify(usuario.to_dict())
    except Usuario.DoesNotExist:
        return jsonify({'status': 404, 'mensagem': 'Postagem não encontrada'})



#try:
#    banco.create_table(Postagem)
#print("OK")
#except Exception as e:
#    pass


# GET /postagens/
@app.route('/usuarios')
def usuarios():
    return jsonify([usuario.to_dict() for usuario in Usuario.select()])

@app.route("/")
def index():
    return "API"

if __name__ == '__main__':
    initialize_db()
    #Postagem = Postagem.create(titulo="Vida", conteudo="Agora Vai!")  # add a new row
    #Postagem.save()  # persist it to db, not necessarily needed
    app.run(host='0.0.0.0', debug = True, port=5050)