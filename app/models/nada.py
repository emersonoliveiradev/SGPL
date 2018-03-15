class UsuarioSchema(Schema):
    class Meta:
        #Fields to expose
        fields = ('nome', 'email','senha','setor')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)




# endpoint to create new user
@app.route("/usuario", methods=["POST"])
def add_usuario():
    if not request.json:
        return jsonify({"Error": "Json não recebido corretamente"}), 404
    nome = request.json['nome']
    email = request.json['email']
    senha = request.json['senha']
    setor = request.json['setor']

    novo_usuario = Usuario(nome, email, senha, setor)

    db.session.add(novo_usuario)
    db.session.commit()
    u = usuario_schema.dump(novo_usuario)
    return jsonify(u), 201

# endpoint to show all users
@app.route("/usuario", methods=["GET"])
def get_usuario():
    all_usuarios = Usuario.query.all()
    result = usuarios_schema.dump(all_usuarios)
    return jsonify(result.data), 201

# endpoint to get user detail by id
@app.route("/usuario/<id>", methods=["GET"])
def usuario_detalhar(id):
    usuario = Usuario.query.get(id)
    u = usuario_schema.dump(usuario)
    return jsonify(u)


# endpoint to update user
@app.route("/usuario/<id>", methods=["PUT"])
def usuario_update(id):
    usuario = Usuario.query.get(id)
    if not request.json:
        return jsonify({"Error": "Json não recebido corretamente"}), 404
    nome = request.json['nome']
    email = request.json['email']
    senha = request.json['senha']
    setor = request.json['setor']

    usuario.nome = nome
    usuario.email = email
    usuario.senha = senha
    usuario.setor = setor


    db.session.commit()
    u = usuario_schema.dump(usuario)
    return jsonify(u)

# endpoint to delete user
@app.route("/usuario/<id>", methods=["DELETE"])
def usuario_delete(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        #u = usuario_schema.dump(usuario)
        return jsonify({'id:': str(usuario.id)})
    else:
        return jsonify({'error': "Este Usuário não existe!"}), 404


# Retornar todos os emails m lista
@app.route("/usuario/email", methods=["GET"])
def usuario_all_emails():
    all_usuarios = Usuario.query.all()
    lst = []
    for i in all_usuarios:
        lst.append(str(i.email))

    return jsonify({"email": lst})


# Retornar todos os emails
@app.route("/usuario/emailxxxxxxxxxxxxxxxxxx", methods=["GET"])
def usuario_all_emailsxxxxxxxxxxxxxxxxxxxxxx():
    print("ok")
    print(requests.get("http://127.0.0.1:5000/usuario/1"))
    print("ok")
    print(all_usuarios)
    return jsonify("ok")

# Retornar todos os emails
@app.route("/usuario/teste", methods=["GET"])
def usuario_all():
    print("ok")
    auth=('e@gmail', '123')
    url = 'http://localhost:5000/'
    r = req.get(url+"usuario", auth=auth)
    print(r)
    return jsonify()