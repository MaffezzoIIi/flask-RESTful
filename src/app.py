from flask import Flask, request, jsonify
from db.banco import Banco
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 

#MODELS
from models.Artistas import Artistas
from models.Clientes import Clientes
from models.Generos import Generos
from models.Gravadoras import Gravadoras
from models.Musicas import Musicas
from models.MusicasArtistas import MusicasArtistas
from models.MusicasClientes import MusicasClientes
from models.Pagamentos import Pagamentos
from models.Planos import Planos


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./banco.db'
    return app

app = create_app()
db = SQLAlchemy(app)

with app.app_context():
     db.create_all()

@app.route('/')
def index():
    return 'Hello, World!'

# CRUD planos
@app.route('/api/planos', methods=['GET'])
def get_planos():
    planos = Planos.query.all()
    return jsonify([plano.serialize() for plano in planos])

@app.route('/api/planos/<int:plano_id>', methods=['GET'])
def get_plano(plano_id):
    plano = Planos.query.get(plano_id)
    if not plano:
        return jsonify({'error': 'Plano não encontrado'}), 404
    return jsonify(plano.serialize())

@app.route('/api/planos', methods=['POST'])
def create_plano():
    data = request.get_json()
    current_time = datetime.utcnow()
    timestamp = int(current_time.timestamp())
    novo_plano = Planos(descricao=data['descricao'], valor=data['valor'], limite=data['limite'], created_at=timestamp, updated_at=timestamp)
    db.session.add(novo_plano)
    db.session.commit()
    return jsonify(novo_plano.serialize()), 201

@app.route('/api/planos/<int:plano_id>', methods=['PUT'])
def update_plano(plano_id):
    plano = Planos.query.get(plano_id)
    if not plano:
        return jsonify({'error': 'Plano não encontrado'}), 404
    
    data = request.get_json()
    plano.descricao = data.get('descricao', plano.descricao)
    plano.valor = data.get('valor', plano.valor)
    plano.limite = data.get('limite', plano.limite)
    current_time = datetime.utcnow()
    plano.updated_at = timestamp = int(current_time.timestamp())

    db.session.commit()
    return jsonify({'message': 'Plano atualizado com sucesso', 'plano': plano.serialize()})

@app.route('/api/planos/<int:plano_id>', methods=['DELETE'])
def delete_plano(plano_id):
    plano = Planos.query.get(plano_id)
    if not plano:
        return jsonify({'error': 'Plano não encontrado'}), 404
    db.session.delete(plano)
    db.session.commit()
    return jsonify({'message': 'Plano excluido com sucesso', 'plano': plano.serialize()})

#CRUD GENEROS
@app.route('/api/generos', methods=['POST'])
def create_genero():
    data = request.get_json()
    current_time = datetime.utcnow()
    timestamp = int(current_time.timestamp())
    novo_genero = Generos(descricao=data['descricao'], created_at=timestamp, updated_at=timestamp)
    db.session.add(novo_genero)
    db.session.commit()
    return jsonify(novo_genero.serialize()), 201

@app.route('/api/generos/<int:genero_id>', methods=['GET'])
def get_genero(genero_id):
    genero = Generos.query.get(genero_id)
    if not genero:
        return jsonify({'error': 'Genero não encontrado'}), 404
    return jsonify(genero.serialize())

@app.route('/api/generos', methods=['GET'])
def get_generos():
    generos = Generos.query.all()
    return jsonify([genero.serialize() for genero in generos])

@app.route('/api/generos/<int:genero_id>', methods=['PUT'])
def update_genero(genero_id):
    genero = Generos.query.get(genero_id)
    if not genero:
        return jsonify({'error': 'Genero não encontrado'}), 404
    data = request.get_json()
    genero.descricao = data.get('descricao', genero.descricao)
    current_time = datetime.utcnow()
    genero.updated_at = timestamp = int(current_time.timestamp())
    db.session.commit()
    return jsonify({'message': 'Genero atualizado com sucesso', 'Genero': genero.serialize()})

@app.route('/api/generos/<int:genero_id>', methods=['DELETE'])
def delete_genero(genero_id):
    genero = Generos.query.get(genero_id)
    if not genero:
        return jsonify({'error': 'Genero não encontrado'}), 404
    db.session.delete(genero)
    db.session.commit()
    return jsonify({'message': 'Genero excluido com sucesso', 'Genero': genero.serialize()})

#CRUD GRAVADORAS
@app.route('/api/gravadoras', methods=['POST'])
def create_gravadora():
    data = request.get_json()
    current_time = datetime.utcnow()
    timestamp = int(current_time.timestamp())
    data_obj = datetime.strptime(data['vencimento_contrato'], "%d/%m/%Y")
    novo_gravadora = Gravadoras(nome=data['nome'], valor_contrato=data['valor_contrato'], vencimento_contrato=int(data_obj.timestamp()), created_at=timestamp, updated_at=timestamp)
    db.session.add(novo_gravadora)
    db.session.commit()
    return jsonify(novo_gravadora.serialize()), 201

@app.route('/api/gravadoras/<int:gravadora_id>', methods=['GET'])
def get_gravadora(gravadora_id):
    gravadora = Gravadoras.query.get(gravadora_id)
    if not gravadora:
        return jsonify({'error': 'Gravadora não encontrado'}), 404
    return jsonify(gravadora.serialize())

@app.route('/api/gravadoras', methods=['GET'])
def get_gravadoras():
    gravadoras = Gravadoras.query.all()
    return jsonify([gravadora.serialize() for gravadora in gravadoras])

@app.route('/api/gravadoras/<int:gravadora_id>', methods=['PUT'])
def update_gravadora(gravadora_id):
    gravadora = Gravadoras.query.get(gravadora_id)
    if not gravadora:
        return jsonify({'error': 'Gravadora não encontrado'}), 404
    
    data = request.get_json()
    gravadora.descricao = data.get('nome', gravadora.nome)
    gravadora.valor_contrato = data.get('valor_contrato', gravadora.valor_contrato)
    data_obj = datetime.strptime(data['vencimento_contrato'], "%d/%m/%Y")
    gravadora.vencimento_contrato = int(data_obj.timestamp())
    current_time = datetime.utcnow()
    gravadora.updated_at = timestamp = int(current_time.timestamp())

    db.session.commit()
    return jsonify({'message': 'Gravadora atualizado com sucesso', 'Gravadora': gravadora.serialize()})

@app.route('/api/gravadoras/<int:gravadora_id>', methods=['DELETE'])
def delete_gravadora(gravadora_id):
    gravadora = Gravadoras.query.get(gravadora_id)
    if not gravadora:
        return jsonify({'error': 'Gravadora não encontrado'}), 404
    db.session.delete(gravadora)
    db.session.commit()
    return jsonify({'message': 'Gravadora excluido com sucesso', 'Gravadora': gravadora.serialize()})

#CRUD clientes
@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()
    current_time = datetime.utcnow()
    timestamp = int(current_time.timestamp())
    novo_cliente = Clientes(login=data['login'], senha=data['senha'], email=data['email'], planos_id=data['email'], created_at=timestamp, updated_at=timestamp)
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify(novo_cliente.serialize()), 201

@app.route('/api/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = Clientes.query.get(cliente_id)
    if not cliente:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    return jsonify(cliente.serialize())

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = Clientes.query.all()
    return jsonify([cliente.serialize() for cliente in clientes])

@app.route('/api/clientes/<int:cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    cliente = Clientes.query.get(cliente_id)
    if not cliente:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    
    data = request.get_json()
    cliente.login = data.get('login', cliente.login)
    cliente.senha = data.get('senha', cliente.senha)
    cliente.planos_id = data.get('planos_id', cliente.planos_id)
    current_time = datetime.utcnow()
    cliente.updated_at = timestamp = int(current_time.timestamp())
    db.session.commit()
    return jsonify({'message': 'Cliente atualizado com sucesso', 'Cliente': cliente.serialize()})

@app.route('/api/clientes/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    cliente = Clientes.query.get(cliente_id)
    if not cliente:
        return jsonify({'error': 'Cliente não encontrado'}), 404
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente excluido com sucesso', 'Cliente': cliente.serialize()})

#CRUD MUSICAS
@app.route('/api/musicas', methods=['GET'])
def get_musicas():
    musicas = Musica.query.all()
    return jsonify([musica.serialize() for musica in musicas])

@app.route('/api/musicas/<int:musica_id>', methods=['GET'])
def get_musica(musica_id):
    musica = Musica.query.get(musica_id)
    if not musica:
        return jsonify({'error': 'Música não encontrada'}), 404
    return jsonify(musica.serialize())

@app.route('/api/musicas', methods=['POST'])
def create_musica():
    data = request.get_json()
    nome = data.get('nome')
    duracao = data.get('duracao')
    generos_id = data.get('generos_id')
    lancamento = data.get('duracao')
    created_at = data.get('created_at')
    updated_at = data.get('updated_at')

    if not titulo or not genero_id or not artista_id:
        return jsonify({'error': 'Campos inválidos'}), 400

    musica = Musica(titulo=titulo, genero_id=genero_id, artista_id=artista_id)
    db.session.add(musica)
    db.session.commit()

    return jsonify({'message': 'Música criada com sucesso', 'musica': musica.serialize()}), 201

@app.route('/api/musicas/<int:musica_id>', methods=['PUT'])
def update_musica(musica_id):
    musica = Musica.query.get(musica_id)
    if not musica:
        return jsonify({'error': 'Música não encontrada'}), 404

    data = request.get_json()
    titulo = data.get('titulo')
    genero_id = data.get('genero_id')
    artista_id = data.get('artista_id')

    if not titulo or not genero_id or not artista_id:
        return jsonify({'error': 'Campos inválidos'}), 400

    musica.titulo = titulo
    musica.genero_id = genero_id
    musica.artista_id = artista_id
    db.session.commit()

    return jsonify({'message': 'Música atualizada com sucesso', 'musica': musica.serialize()})

@app.route('/api/musicas/<int:musica_id>', methods=['DELETE'])
def delete_musica(musica_id):
    musica = Musica.query.get(musica_id)
    if not musica:
        return jsonify({'error': 'Musica não encontrado'}), 404
    db.session.delete(musica)
    db.session.commit()
    return jsonify({'message': 'Musica excluido com sucesso', 'Musica': musica.serialize()})

#CRUD artistas
@app.route('/api/artistas', methods=['GET'])
def get_artistas():
    artistas = Artista.query.all()
    return jsonify([artista.serialize() for artista in artistas])

@app.route('/api/artistas/<int:artista_id>', methods=['GET'])
def get_artista(artista_id):
    artista = Artista.query.get(artista_id)
    if not artista:
        return jsonify({'error': 'Artista não encontrado'}), 404
    return jsonify(artista.serialize())

@app.route('/api/artistas', methods=['POST'])
def create_artista():
    data = request.get_json()
    nome = data.get('nome')
    gravadora_id = data.get('gravadora_id')

    if not nome or not gravadora_id:
        return jsonify({'error': 'Campos inválidos'}), 400

    artista = Artista(nome=nome, gravadora_id=gravadora_id)
    db.session.add(artista)
    db.session.commit()

    return jsonify({'message': 'Artista criado com sucesso', 'artista': artista.serialize()}), 201

@app.route('/api/artistas/<int:artista_id>', methods=['PUT'])
def update_artista(artista_id):
    artista = Artista.query.get(artista_id)
    if not artista:
        return jsonify({'error': 'Artista não encontrado'}), 404

    data = request.get_json()
    nome = data.get('nome')
    gravadora_id = data.get('gravadora_id')

    if not nome or not gravadora_id:
        return jsonify({'error': 'Campos inválidos'}), 400

    artista.nome = nome
    artista.gravadora_id = gravadora_id
    db.session.commit()

    return jsonify({'message': 'Artista atualizado com sucesso', 'Artista': artista.serialize()})

@app.route('/api/artistas/<int:artista_id>', methods=['DELETE'])
def delete_artista(artista_id):
    artista = Artista.query.get(artista_id)
    if not artista:
        return jsonify({'error': 'Artista não encontrado'}), 404

    db.session.delete(artista)
    return jsonify({'message': 'Artista excluido com sucesso', 'Artista': artista.serialize()})

@app.route('/api/musicas_has_artistas', methods=['GET'])
def get_musicas_artistas():
    query = db.session.query(Musica.nome, Artista.nome).join(MusicasArtistas).join(Artista)
    result = query.all()
    data = [{'musica': row[0], 'artista': row[1]} for row in result]
    return jsonify(data)

if __name__ == '__main__':
    app.run()