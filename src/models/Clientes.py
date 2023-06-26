from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Clientes(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    login = db.Column(db.Text, nullable=False)
    senha = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text)
    planos_id = db.Column(db.Integer,  db.ForeignKey('planos.id'), nullable=False)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'valor_contrato': self.valor_contrato,
            'vencimento_contrato': datetime.fromtimestamp(self.vencimento_contrato).isoformat(),
            'created_at': datetime.fromtimestamp(self.created_at).isoformat(),
            'updated_at': datetime.fromtimestamp(self.updated_at).isoformat()
        }