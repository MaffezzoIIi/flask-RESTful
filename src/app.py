from flask import Flask, request, jsonify
from datetime import datetime

from src.models.Planos import Planos
from src.models.Generos import Generos
from src.models.Gravadoras import Gravadoras

def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/planos', methods=['GET'])
def get_planos():
    return 'api/planos'


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
        plano = Planos(data['nome_plano'],
                       data['valor_plano'], data['descricao'])
        plano.setCreated_at(datetime.now())
        plano.setUpdated_at(datetime.now())


        plano.save()

        return jsonify(plano.__dict__), 200

    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/planos/<int:plano_id>', methods=['PUT'])
def update_plano(plano_id):
    plano = Planos().getOne(plano_id)

    if plano is not None:
        data = request.get_json()

        plano.update(data)

        return jsonify(plano.__dict__), 200


    return jsonify({'message': 'Nenhum plano encontrato com este id'}), 400


@app.route('/api/planos/<int:plano_id>', methods=['DELETE'])
def delete_plano(plano_id):
    if(Planos().remove(plano_id)):
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
        gravadora = Gravadoras(data['nome'], data['valor_contrato'], data['vencimento_contrato'])
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
    gravadora = Gravadoras.getOne(gravadora_id)

    if gravadora is not None:
        data = request.get_json()

        gravadora.update(data)

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
    return 'cliente'


@app.route('/api/clientes/<int:cliente_id>', methods=['GET'])
def get_cliente(cliente_id):
    return 'cliente'


@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return 'cliente'


@app.route('/api/clientes/<int:cliente_id>', methods=['PUT'])
def update_cliente(cliente_id):
    return 'cliente'


@app.route('/api/clientes/<int:cliente_id>', methods=['DELETE'])
def delete_cliente(cliente_id):
    return 'cliente'

# CRUD MUSICAS


@app.route('/api/musicas', methods=['GET'])
def get_musicas():
    return 'cliente'


@app.route('/api/musicas/<int:musica_id>', methods=['GET'])
def get_musica(musica_id):
    return 'cliente'


@app.route('/api/musicas', methods=['POST'])
def create_musica():
    return 'cliente'


@app.route('/api/musicas/<int:musica_id>', methods=['PUT'])
def update_musica(musica_id):
    return 'cliente'


@app.route('/api/musicas/<int:musica_id>', methods=['DELETE'])
def delete_musica(musica_id):
    return 'cliente'

# CRUD artistas


@app.route('/api/artistas', methods=['GET'])
def get_artistas():
    return 'cliente'


@app.route('/api/artistas/<int:artista_id>', methods=['GET'])
def get_artista(artista_id):
    return 'cliente'


@app.route('/api/artistas', methods=['POST'])
def create_artista():
    return 'cliente'


@app.route('/api/artistas/<int:artista_id>', methods=['PUT'])
def update_artista(artista_id):
    return 'cliente'


@app.route('/api/artistas/<int:artista_id>', methods=['DELETE'])
def delete_artista(artista_id):
    return 'cliente'


@app.route('/api/musicas_has_artistas', methods=['GET'])
def get_musicas_artistas():
    return 'cliente'


if __name__ == '__main__':
    app.run()
