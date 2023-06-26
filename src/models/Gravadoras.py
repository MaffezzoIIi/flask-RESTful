from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Gravadoras(db.Model):
    id = db.Column(db.Integer,nullable=False, primary_key=True, autoincrement=True)
    nome = db.Column(db.Text, nullable=False)
    valor_contrato = db.Column(db.DECIMAL(10,0), nullable=False)
    vencimento_contrato = db.Column(db.Integer)
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