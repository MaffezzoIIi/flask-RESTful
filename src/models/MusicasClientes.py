from src.db.banco import Banco

mydb = Banco()

class MusicasClientes():

    def __init__(self, musica_id, clientes_id):
        self.musica_id = musica_id
        self.clientes_id = clientes_id

    def getMusica_id(self):
        return self.musica_id

    def setMusica_id(self, musica_id):
        self.musica_id = musica_id

    def getClientes_id(self):
        return self.clientes_id

    def setClientes_id(self, clientes_id):
        self.clientes_id = clientes_id


    def save(musicas_clientes):
        cursor = mydb.getCursor()

        sql = "INSERT INTO musicas_clientes (musica_id, clientes_id) VALUES (%s, %s)"
        val = (musicas_clientes.getMusica_id(), musicas_clientes.getClientes_id())

        cursor.execute(sql, val)
        mydb.commit()

        return musicas_clientes
    
    def removeByMusicas(musica_id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM musicas_clientes WHERE musica_id = %s"
        val = (musica_id,)

        cursor.execute(sql, val)
        mydb.commit()

        return True
    
    def removeByClientes(clientes_id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM musicas_clientes WHERE clientes_id = %s"
        val = (clientes_id,)

        cursor.execute(sql, val)
        mydb.commit()

        return True
    
    def getClientesByMusica(musica_id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM musicas_clientes WHERE musica_id = %s"
        val = (musica_id,)

        cursor.execute(sql, val)
        myresult = cursor.fetchall()

        return myresult
    
    def getMusicasByCliente(clientes_id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM musicas_clientes WHERE clientes_id = %s"
        val = (clientes_id,)

        cursor.execute(sql, val)
        myresult = cursor.fetchall()

        return myresult