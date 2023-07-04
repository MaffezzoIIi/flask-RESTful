from flask import Flask, request, jsonify
from datetime import datetime

from src.models.Planos import Planos
from src.models.Generos import Generos
from src.models.Gravadoras import Gravadoras
from src.models.Clientes import Clientes
from src.models.Musicas import Musicas
from src.models.Artistas import Artistas

def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/planos', methods=['GET'])
def get_planos():
    planos = Planos.getAll()
    
    if planos is not None:
        return jsonify(planos), 200
    
    return  jsonify({'message': 'Nenhum genero encontrado'}), 400


@app.route('/api/planos/<int:plano_id>', methods=['GET'])
def get_plano(plano_id):
    plano = Planos.getOne(plano_id)
    return jsonify(plano.__dict__), 200


@app.route('/api/planos', methods=['POST'])
def create_plano():
    data = request.get_json()
    print(data)

    if(len(data['descricao']) > 45):
        return jsonify({'message': 'Descricao muito grande'}), 400

    if data is not None:
        plano = Planos(None, data['nome_plano'],
                       data['valor_plano'], data['descricao'])
        plano.setCreated_at(datetime.now())
        plano.setUpdated_at(datetime.now())


        plano.save()

        return jsonify(plano.__dict__), 200

    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/planos/<int:plano_id>', methods=['PUT'])
def update_plano(plano_id):
    data = request.get_json()
    
    if data is not None:
        planos = Planos.update(data, plano_id)

        return jsonify(planos.__dict__), 200


    return jsonify({'message': 'Nenhum plano encontrato com este id'}), 400


@app.route('/api/planos/<int:plano_id>', methods=['DELETE'])
def delete_plano(plano_id):
    if(Planos.remove(plano_id)):
        return jsonify({'message': 'Plano removido com sucesso'}), 200


    return jsonify({'message': 'Nenhum plano encontrato com este id'}), 400

# CRUD GENEROS
@app.route('/api/generos', methods=['POST'])
def create_genero():
    data = request.get_json()

    if data is not None:
        genero = Generos(data['descricao'])
        genero.setCreated_at(datetime.now())
        genero.setUpdated_at(datetime.now())

        genero.save()

        return jsonify(genero.__dict__), 200
    
    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/generos/<int:genero_id>', methods=['GET'])
def get_genero(genero_id):
    genero = Generos.getOne(genero_id)

    if genero is not None:
        return jsonify(genero.__dict__), 200
    
    return jsonify({'message': 'Nenhum genero encontrado com este id'}), 400


@app.route('/api/generos', methods=['GET'])
def get_generos():
    generos = Generos.getAll()

    if generos is not None:
        return jsonify(generos), 200
    
    return  jsonify({'message': 'Nenhum genero encontrado'}), 400


@app.route('/api/generos/<int:genero_id>', methods=['PUT'])
def update_genero(genero_id):
    genero = Generos.getOne(genero_id)

    if genero is not None:
        data = request.get_json()

        genero.update(data)

        return jsonify(genero.__dict__), 200
    
    return jsonify({'message': 'Nenhum genero encontrado com este id'}), 400


@app.route('/api/generos/<int:genero_id>', methods=['DELETE'])
def delete_genero(genero_id):
    if(Generos.remove(genero_id)):
        return jsonify({'message': 'Genero removido com sucesso'}), 200
    
    return jsonify({'message': 'Nenhum genero encontrado com este id'}), 400

# CRUD GRAVADORAS
@app.route('/api/gravadoras', methods=['POST'])
def create_gravadora():
    data = request.get_json()

    if data is not None:
        data_datetime = datetime.strptime(data['vencimento_contrato'], "%d/%m/%Y")
        gravadora = Gravadoras(None, data['nome'], data['valor_contrato'], data_datetime.date())
        gravadora.setCreated_at(datetime.now())
        gravadora.setUpdated_at(datetime.now())

        gravadora.save()

        return jsonify(gravadora.__dict__), 200

    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/gravadoras/<int:gravadora_id>', methods=['GET'])
def get_gravadora(gravadora_id):
    gravadora = Gravadoras.getOne(gravadora_id)

    if gravadora is not None:
        return jsonify(gravadora.__dict__), 200
    
    return jsonify({'message': 'Nenhuma gravadora encontrada com este id'}), 400


@app.route('/api/gravadoras', methods=['GET'])
def get_gravadoras():
    gravadoras = Gravadoras.getAll()

    if gravadoras is not None:
        return jsonify(gravadoras), 200
    
    return jsonify({'message': 'Nenhuma gravadora encontrada'}), 400


@app.route('/api/gravadoras/<int:gravadora_id>', methods=['PUT'])
def update_gravadora(gravadora_id):
    data = request.get_json()
    
    if data is not None:    
        gravadora = Gravadoras.update   (data, gravadora_id)

        return jsonify(gravadora.__dict__), 200
    
    return jsonify({'message': 'Nenhuma gravadora encontrada com este id'}), 400


@app.route('/api/gravadoras/<int:gravadora_id>', methods=['DELETE'])
def delete_gravadora(gravadora_id):
    if(Gravadoras.remove(gravadora_id)):
        return jsonify({'message': 'Gravadora removida com sucesso'}), 200
    
    return jsonify({'message': 'Nenhuma gravadora encontrada com este id'}), 400

# CRUD clientes
@app.route('/api/clientes', methods=['POST'])
def create_cliente():
    data = request.get_json()

    if data is not None:
        cliente = Clientes(data['login'], data['senha'], data['email'], data['planos_id'])
        cliente.setCreated_at(datetime.now())
        cliente.setUpdated_at(datetime.now())

        cliente.save()

        return jsonify(cliente.__dict__), 200
    
    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    cliente = Clientes.getOne(cliente_id)

    if cliente is not None:
        return jsonify(cliente.__dict__), 200
    
    return jsonify({'message': 'Nenhum cliente encontrado com este id'}), 400


@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    clientes = Clientes.getAll()

    if clientes is not None:
        return jsonify(clientes), 200
    
    return jsonify({'message': 'Nenhum cliente encontrado'}), 400


@app.route('/api/clientes/<int:cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    cliente = Clientes.getOne(cliente_id)

    if cliente is not None:
        data = request.get_json()

        cliente.update(data)

        return jsonify(cliente.__dict__), 200
    return jsonify({'message': 'Nenhum cliente encontrado com este id'}), 400


@app.route('/api/clientes/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    if(Clientes.remove(cliente_id)):
        return jsonify({'message': 'Cliente removido com sucesso'}), 200
    
    return jsonify({'message': 'Nenhum cliente encontrado com este id'}), 400

# CRUD MUSICAS
@app.route('/api/musicas', methods=['GET'])
def get_musicas():
    return 'cliente'


@app.route('/api/musicas/<int:musica_id>', methods=['GET'])
def get_musica(musica_id):
    musica = Musicas.getOne(musica_id)

    if musica is not None:
        return jsonify(musica.__dict__), 200
    
    return jsonify({'message': 'Nenhuma musica encontrada com este id'}), 400


@app.route('/api/musicas', methods=['POST'])
def create_musica():
    data = request.get_json()

    if data is not None:
        musica = Musicas(data['nome'], data['duracao'], data['generos_id'], data['lancamento'])
        musica.setCreated_at(datetime.now())
        musica.setUpdated_at(datetime.now())

        musica.save()

        return jsonify(musica.__dict__), 200
    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/musicas/<int:musica_id>', methods=['PUT'])
def update_musica(musica_id):
    musica = Musicas.getOne(musica_id)

    if musica is not None:
        data = request.get_json()

        musica.update(data)

        return jsonify(musica.__dict__), 200
    
    return jsonify({'message': 'Nenhuma musica encontrada com este id'}), 400


@app.route('/api/musicas/<int:musica_id>', methods=['DELETE'])
def delete_musica(musica_id):
    if(Musicas.remove(musica_id)):
        return jsonify({'message': 'Musica removida com sucesso'}), 200
    
    return jsonify({'message': 'Nenhuma musica encontrada com este id'}), 400

# CRUD artistas
@app.route('/api/artistas', methods=['GET'])
def get_artistas():

    return 'cliente'


@app.route('/api/artistas/<int:artista_id>', methods=['GET'])
def get_artista(artista_id):
    return 'cliente'


@app.route('/api/artistas', methods=['POST'])
def create_artista():
    data = request.get_json()

    if data is not None:
        artista = Artistas(data['nome'], data['gravadoras_id'])
        artista.setCreated_at(datetime.now())
        artista.setUpdated_at(datetime.now())

        artista.save()

        return jsonify(artista.__dict__), 200

    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/artistas/<int:artista_id>', methods=['PUT'])
def update_artista(artista_id):
    artista = Artistas.getOne(artista_id)

    if artista is not None:
        data = request.get_json()

        artista.update(data)

        return jsonify(artista.__dict__), 200
    
    return jsonify({'message': 'Nenhum artista encontrado com este id'}), 400


@app.route('/api/artistas/<int:artista_id>', methods=['DELETE'])
def delete_artista(artista_id):
    if(Artistas.remove(artista_id)):
        return jsonify({'message': 'Artista removido com sucesso'}), 200
    
    return jsonify({'message': 'Nenhum artista encontrado com este id'}), 400


if __name__ == '__main__':
    app.run()
