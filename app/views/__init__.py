from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from flask import jsonify

from app import api, db
from app.models.tables import Setor, Usuario
#from app.models import Usuario
#from app.models import Setor

#Usuarios
class UsuariosResource(Resource):
    def get(self, usuario_id):
        usuario = db.session.query(Usuario).filter_by(id=usuario_id).first()
        if not usuario:
            return {'message': 'Not found'}, 404
        return {usuario_id: usuario.nome} #Tem q serializar o setor e enviar ele todo!!!
        #return [{usuario_id: usuario.nome} for usuario in db.session.query(Usuario).filter_by(id=usuario_id).all() ]#Tem q serializar o setor e enviar ele todo!!!

    def put(self, usuario_id):
        usuario = db.session.query(Usuario).filter_by(id=usuario_id).first()
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        usuario.senha = request.form['senha']
        usuario.setor = request.form['setor']
        usuario.tipo = request.form['tipo']
        db.session.commit()
        return {usuario_id: usuario.nome}

    def delete(self, usuario_id):
        try:
            usuario = Usuario.query.get(usuario_id)
            print(usuario)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
            return jsonify({'status': 200, 'mensagem': 'Usuario excluída com sucesso'})

        except :
            return jsonify({'status': 404, 'mensagem': 'Usuario não encontrada'})

class UsuariosListResource(Resource):
    def get(self):
        return [{usuario.id: {'nome': usuario.nome, 'email': usuario.email, 'setor': usuario.setor, 'tipo': usuario.tipo}} for usuario in db.session.query(Usuario).all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('senha', required=True)
        parser.add_argument('setor', type=int, required=True)
        parser.add_argument('tipo', type=int, required=True)
        args = parser.parse_args()

        if not 'nome' in args or not 'email' in args or not 'senha' in args or not 'setor' in args or not 'tipo' in args:
            # we return bad request since we require name and color
            return {'message': 'Missing required parameters.'}, 400

        new_usuario = Usuario(nome=args['nome'], email=args['email'], senha=args['senha'], setor=args['setor'], tipo=args['tipo'])
        db.session.add(new_usuario)
        db.session.commit()
        usuario = new_usuario # Ajeito ;/
        return {new_usuario.id: {'nome': usuario.nome, 'email': usuario.senha, 'senha': usuario.senha, 'setor': usuario.setor, 'tipo': usuario.tipo}}, 201

class SetoresResource(Resource):
    def get(self, setor_id):
        setor = db.session.query(Setor).filter_by(id=setor_id).first()
        if not setor:
            return {'message': 'Not found'}, 404
        return {setor_id: setor.nome} #Tem q serializar o setor e enviar ele todo!!!

    def put(self, setor_id):
        setor = db.session.query(Setor).filter_by(id=setor_id).first()
        setor.nome = request.form['nome']
        db.session.commit()
        return {setor_id: setor.nome}

    def delete(self, setor_id):
        try:
            setor = Setor.query.get(setor_id)
            if setor:
                db.session.delete(setor)
                db.session.commit()
            return jsonify({'status': 200, 'mensagem': 'Setor excluída com sucesso'})

        except :
            return jsonify({'status': 404, 'mensagem': 'Setor não encontrada'})

class SetoresListResource(Resource):
    def get(self):
        return [{setor.id: {'nome': setor.nome}} for setor in db.session.query(Setor).all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nome')

        args = parser.parse_args()
        if not 'nome':
            return {'message': 'Missing required parameters.'}, 400

        new_setor = Setor(nome=args['nome'])
        db.session.add(new_setor)
        db.session.commit()
        setor = new_setor  # Ajeito ;/
        return {new_setor.id: {'nome': setor.nome}}, 201


#Resources
api.add_resource(SetoresResource, '/api/v1/setor/<setor_id>')
api.add_resource(SetoresListResource, '/api/v1/setores')

api.add_resource(UsuariosResource, '/api/v1/usuario/<usuario_id>')
api.add_resource(UsuariosListResource, '/api/v1/usuarios')