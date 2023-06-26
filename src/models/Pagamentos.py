from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pagamentos(db.Model):
    id = db.Column(db.Integer,nullable=False, primary_key=True, autoincrement=True)
    date = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'id': self.id,
            'date': datetime.fromtimestamp(self.date).isoformat()
        }