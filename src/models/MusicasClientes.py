from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MusicasClientes(db.Model):
    __tablename__ = 'musicas_has_clientes'
    musica_id = db.Column(db.Integer, db.ForeignKey('musicas.id'), primary_key=True)
    clientes_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), primary_key=True)
    musica = db.relationship('Musicas', backref=db.backref('musicas_has_clientes', cascade='all, delete-orphan'))
    cliente = db.relationship('Clientes', backref=db.backref('musicas_has_clientes', cascade='all, delete-orphan'))