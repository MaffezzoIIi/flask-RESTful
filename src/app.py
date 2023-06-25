from flask import Flask, request, jsonify
from db.banco import Banco
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# from plano import Plano

# Banco()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./banco.db'
    return app

app = create_app()
db = SQLAlchemy(app)
# db.create_all()

@app.route('/')
def index():
    return 'Hello, World!'


class Planos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text)
    valor = db.Column(db.DECIMAL(5, 2))
    limite = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'valor': self.valor,
            'limite': self.limite,
            'created_at': datetime.fromtimestamp(self.created_at).isoformat(),
            'updated_at': datetime.fromtimestamp(self.updated_at).isoformat()
        }

with app.app_context():
     db.create_all()

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


if __name__ == '__main__':
    app.run()