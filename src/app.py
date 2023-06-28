from flask import Flask, request, jsonify
from datetime import datetime

from src.models.Planos import Planos


def create_app():
    app = Flask(__name__)
    return app


app = create_app()


@app.route('/')
def index():
    return 'Hello, World!'

# CRUD planos


@app.route('/api/planos', methods=['GET'])
def get_planos():
    return 'api/planos'


@app.route('/api/planos/<int:plano_id>', methods=['GET'])
def get_plano(plano_id):
    return 'api/planos'


@app.route('/api/planos', methods=['POST'])
def create_plano():
    data = request.get_json()
    print(data)

    if data is not None:
        plano = Planos(data['id_plano'], data['nome_plano'],
                       data['valor_plano'], data['descricao_plano'])
        plano.setCreated_at(datetime.now())
        plano.setUpdated_at(datetime.now())

        return jsonify(plano.__dict__), 200

    return jsonify({'message': 'No data provided'}), 400


@app.route('/api/planos/<int:plano_id>', methods=['PUT'])
def update_plano(plano_id):
    return 'api/planos'


@app.route('/api/planos/<int:plano_id>', methods=['DELETE'])
def delete_plano(plano_id):
    return 'api/planos'

# CRUD GENEROS


@app.route('/api/generos', methods=['POST'])
def create_genero():
    return 'api/generos'


@app.route('/api/generos/<int:genero_id>', methods=['GET'])
def get_genero(genero_id):
    return 'api/generos'


@app.route('/api/generos', methods=['GET'])
def get_generos():
    return 'api/generos'


@app.route('/api/generos/<int:genero_id>', methods=['PUT'])
def update_genero(genero_id):
    return 'api/generos'


@app.route('/api/generos/<int:genero_id>', methods=['DELETE'])
def delete_genero(genero_id):
    return 'api/generos'

# CRUD GRAVADORAS


@app.route('/api/gravadoras', methods=['POST'])
def create_gravadora():
    return 'gravadoras'


@app.route('/api/gravadoras/<int:gravadora_id>', methods=['GET'])
def get_gravadora(gravadora_id):
    return 'gravadoras'


@app.route('/api/gravadoras', methods=['GET'])
def get_gravadoras():
    return 'gravadoras'


@app.route('/api/gravadoras/<int:gravadora_id>', methods=['PUT'])
def update_gravadora(gravadora_id):
    return 'gravadoras'


@app.route('/api/gravadoras/<int:gravadora_id>', methods=['DELETE'])
def delete_gravadora(gravadora_id):
    return 'gravadoras'

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
