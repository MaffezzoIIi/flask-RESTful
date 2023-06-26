from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MusicasArtistas(db.Model):
    __tablename__ = 'musicas_has_artistas'
    musica_id = db.Column(db.Integer, db.ForeignKey('musica.id'), primary_key=True)
    artista_id = db.Column(db.Integer, db.ForeignKey('artista.id'), primary_key=True)
    musica = db.relationship('Musica', backref=db.backref('musicas_has_artistas', cascade='all, delete-orphan'))
    artista = db.relationship('Artista', backref=db.backref('musicas_has_artistas', cascade='all, delete-orphan'))