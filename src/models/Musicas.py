from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Musicas(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    nome = db.Column(db.Text, nullable=False)
    duracao = db.Column(db.Time, nullable=False)
    generos_id = db.Column(db.Integer, db.ForeignKey('generos.id'), nullable=False)
    lancamento = db.Column(db.Integer)
    created_at = db.Column(db.Integer)
    updated_at = db.Column(db.Integer)
    artistas = db.relationship('Artista', secondary='musicas_has_artistas', backref='musicas')

    def serialize(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero.nome,
            'artista': self.artista.nomes
        }