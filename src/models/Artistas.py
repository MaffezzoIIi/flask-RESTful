from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Artistas(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = db.Column(db.Text, nullable=False)
    gravadoras_id = db.Column(db.INTEGER, db.ForeignKey('gravadoras.id'), nullable=False)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    musicas = db.relationship('Musica', secondary='musicas_has_artistas', backref='artistas')

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'gravadoras': self.gravadoras.nome,
            'created_at': datetime.fromtimestamp(self.created_at).isoformat(),
            'updated_at': datetime.fromtimestamp(self.updated_at).isoformat()
        }