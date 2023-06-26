from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.init_app(app)

class Generos(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    descricao = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'created_at': datetime.fromtimestamp(self.created_at).isoformat(),
            'updated_at': datetime.fromtimestamp(self.updated_at).isoformat()
        }