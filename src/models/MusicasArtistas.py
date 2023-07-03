from src.db.banco import Banco

mydb = Banco()

class MusicasArtistas():

    def __init__(self, musica_id, artista_id):
        self.musica_id = musica_id
        self.artista_id = artista_id

    def getMusica_id(self):
        return self.musica_id

    def setMusica_id(self, musica_id):
        self.musica_id = musica_id

    def getArtista_id(self):
        return self.artista_id

    def setArtista_id(self, artista_id):
        self.artista_id = artista_id

    def save(musicas_artistas):
        cursor = mydb.getCursor()

        sql = "INSERT INTO musicas_artistas (musica_id, artista_id) VALUES (%s, %s)"
        val = (musicas_artistas.getMusica_id(), musicas_artistas.getArtista_id())

        cursor.execute(sql, val)
        mydb.commit()

        return musicas_artistas
    
    def removeByMusicas(musica_id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM musicas_artistas WHERE musica_id = %s"
        val = (musica_id,)

        cursor.execute(sql, val)
        mydb.commit()

        return True
    
    def removeByArtistas(artista_id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM musicas_artistas WHERE artista_id = %s"
        val = (artista_id,)

        cursor.execute(sql, val)
        mydb.commit()

        return True
    
    def getArtistasByMusica(musica_id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM musicas_artistas WHERE musica_id = %s"
        val = (musica_id,)

        cursor.execute(sql, val)
        result = cursor.fetchall()

        return result
    
    def getMusicasByArtista(artista_id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM musicas_artistas WHERE artista_id = %s"
        val = (artista_id,)

        cursor.execute(sql, val)
        result = cursor.fetchall()

        return result