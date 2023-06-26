from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Planos(db.Model):
    id = db.Column(db.Integer,nullable=False, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text, nullable=False)
    valor = db.Column(db.DECIMAL(5, 2),nullable=False)
    limite = db.Column(db.Integer,nullable=False)
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

    def get_planos(self, plano_id):
        return self.query.get(plano_id)

    def update_plano(self, plano_id, descricao=None, valor=None, limite=None):
        plano = self.get_plano(plano_id)
        if not plano:
            raise ValueError("Plano não encontrado")
        
        if descricao is not None:
            plano.descricao = descricao
        if valor is not None:
            plano.valor = valor
        if limite is not None:
            plano.limite = limite
        
        plano.updated_at = int(datetime.now().timestamp())
        self.commit()
