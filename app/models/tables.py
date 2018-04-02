from app import db

###########################################setores
class Setor(db.Model):
    __tablename__ = "setores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))

    def __init__(self, nome):
        self.nome = nome


###########################################usuarios
class Usuario(db.Model):
    #Create table
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    senha = db.Column(db.String(50))
    tipo = db.Column(db.Integer)
    setor = db.Column(db.Integer, db.ForeignKey('setores.id'))
    #setor = db.relationship('Setor', foreign_keys=setor.id)

    def __init__(self, nome, email, senha, tipo, setor):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.setor = setor

#Métodos para gerenciamento do Flask-login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<Usuario {}>'.format(self.nome)



###########################################produtos
class Produto(db.Model):
    #Create table
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    catmat = db.Column(db.String(50), unique=True)

    def __init__(self, nome, catmat):
        self.nome = nome
        self.catmat = catmat



###########################################fornecedores
class Fornecedor(db.Model):
    #Create table
    __tablename__ = "fornecedores"

    id = db.Column(db.Integer, primary_key=True)
    razao_social = db.Column(db.String(50))
    nome_fantasia = db.Column(db.String(50))
    email = db.Column(db.String(50))
    cnpj = db.Column(db.String(11))
    telefone = db.Column(db.String(20))
    #Criar atributo booleano "ativo"
    def __init__(self, razao_social, nome_fantasia, email, cnpj, telefone):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.email = email
        self.cnpj = cnpj
        self.telefone = telefone



#Não deveria ter ID
###########################################fornecedore_fornece_produto
class Fornecedor_Fornece_Produto(db.Model):
    #Create table
    __tablename__ = "fornecedor_fornece_produto"

    id = db.Column(db.Integer, primary_key=True)
    fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    produto = db.Column(db.Integer, db.ForeignKey('produtos.id'))

    def __init__(self, fornecedor, produto):
        self.fornecedor = fornecedor
        self.produto = produto



###########################################pedidos
class Pedido(db.Model):
    __tablename__ = "pedidos"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50))
    usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    requisitante = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __init__(self, data, requisitante, usuario):
        self.data = data
        self.usuario = usuario
        self.requisitante = requisitante



###########################################itens_do_pedido
class Item_do_Pedido(db.Model):
    __tablename__ = "itens_do_pedido"

    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer)
    fornecedor1 = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    fornecedor2 = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    fornecedor3 = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    valor_fornecedor1 = db.Column(db.Numeric)
    valor_fornecedor2 = db.Column(db.Numeric)
    valor_fornecedor3 = db.Column(db.Numeric)
    produto = db.Column(db.Integer, db.ForeignKey('produtos.id'))

    def __init__(self, quantidade, fornecedor1, fornecedor2, forncedor3, valor_forncedor1, valor_forncedor2, valor_forncedor3, produto):
        self.quantidade = quantidade
        self.fornecedor1 = fornecedor1
        self.fornecedor2 = fornecedor2
        self.fornecedor3 = forncedor3
        self.valor_fornecedor1 = valor_forncedor1
        self.valor_fornecedor2 = valor_forncedor2
        self.valor_fornecedor3 = valor_forncedor3
        self.produto = produto



#Não deveria ter ID
###########################################pedido_tem_item_do_pedido
class Pedido_tem_Item_do_Pedido(db.Model):
    __tablename__ = "pedido_tem_item_do_pedido"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    itens_do_pedido = db.Column(db.Integer, db.ForeignKey('itens_do_pedido.id'))

    def __init__(self, status, pedido, item_do_pedido):
        self.status = status
        self.pedido = pedido
        self.itens_do_pedido = item_do_pedido



###########################################pregoes
class Pregao(db.Model):
    __tablename__ = "pregoes"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50))
    pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    item_pregao = db.Column(db.Integer, db.ForeignKey('itens_do_pregao.id'))

    def __init__(self, data, pedido, item_pregao):
        self.data = data
        self.pedido = pedido
        self.item_pregao = item_pregao

    # Return informations about User
    def __repr__(self):
        return "<Pregões %r>" % self.id



###########################################itens_do_pregao
class Item_do_Pregao(db.Model):
    __tablename__ = "itens_do_pregao"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    valor_referencia = db.Column(db.Numeric)
    pregao = db.Column(db.Integer, db.ForeignKey('pregoes.id'))
    produto = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    fornecedor = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))

    def __init__(self, data, quantidade, valor_referencia, pregao, produto, fornecedor):
        self.data = data
        self.quantidade = quantidade
        self.valor_referencia = valor_referencia
        self.pregao = pregao
        self.produto = produto
        self.fornecedor = fornecedor



###########################################pregao_tem_item_do_pregao
class Pregao_tem_Item_do_Pregao(db.Model):
    #Create table
    __tablename__ = "pregao_tem_item_do_pregao"

    id = db.Column(db.Integer, primary_key=True)
    pregao = db.Column(db.Integer, db.ForeignKey('pregoes.id'))
    itens_do_pregao = db.Column(db.Integer, db.ForeignKey('itens_do_pregao.id'))

    def __init__(self, pregao, itens_do_pregao):
        self.pregao = pregao
        self.itens_do_pregao = itens_do_pregao

