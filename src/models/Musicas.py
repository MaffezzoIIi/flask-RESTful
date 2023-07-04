import datetime
from src.db.banco import Banco

mydb = Banco()

class Musicas():

    def __init__(self, id, nome, duracao, generos_id, lancamento):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.generos_id = generos_id
        self.lancamento = lancamento
        self.created_at = None
        self.updated_at = None

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getDuracao(self):
        return self.duracao

    def setDuracao(self, duracao):
        self.duracao = duracao

    def getGeneros_id(self):
        return self.generos_id

    def setGeneros_id(self, generos_id):
        self.generos_id = generos_id

    def getLancamento(self):
        return self.lancamento

    def setLancamento(self, lancamento):
        self.lancamento = lancamento

    def created_at(self):
        return self.created_at

    def setCreated_at(self, created_at):
        self.created_at = created_at

    def updated_at(self):
        return self.updated_at

    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at


    def save(musica):
        cursor = mydb.getCursor()

        sql = "INSERT INTO musicas (nome, duracao, generos_id, lancamento, created, modified) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (musica.getNome(), musica.getDuracao(), musica.getGeneros_id(), musica.getLancamento(), musica.created_at, musica.created_at)

        musica.setId(cursor.lastrowid)

        cursor.execute(sql, val)
        mydb.commit()

        return musica
    
    def getOne(id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM musicas WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)

        result = cursor.fetchone()

        return result
    
    def getAll():
        cursor = mydb.getCursor()

        cursor.execute("SELECT * FROM musicas")
        myresult = cursor.fetchall()

        return myresult
    
    def update(musica):
        cursor = mydb.getCursor()

        musica.setUpdated_at(datetime.now())

        sql = "UPDATE musicas SET nome = %s, duracao = %s, generos_id = %s, lancamento = %s, updated_at = %s WHERE id = %s"
        val = (musica.getNome(), musica.getDuracao(), musica.getGeneros_id(), musica.getLancamento(), musica.updated_at, musica.getId())

        cursor.execute(sql, val)
        mydb.commit()

        return musica
    
    def remove(id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM musicas WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)
        mydb.commit()

        return True