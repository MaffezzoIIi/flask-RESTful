import datetime
from src.db.banco import Banco

mydb = Banco()

class Artistas():

    def __init__(self, id, nome, gravadoras_id, created_at, updated_at):
        self.id = id
        self.nome = nome
        self.gravadoras_id = gravadoras_id
        self.created_at = created_at
        self.updated_at = updated_at

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getGravadoras_id(self):
        return self.gravadoras_id

    def setGravadoras_id(self, gravadoras_id):
        self.gravadoras_id = gravadoras_id

    def getCreated_at(self):
        return self.created_at

    def setCreated_at(self, created_at):
        self.created_at = created_at

    def getUpdated_at(self):
        return self.updated_at

    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at

    def save(gravadora):
        cursor = mydb.getCursor()

        sql = "INSERT INTO gravadoras (nome, valor_contrato, vencimento_contrato, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
        val = (gravadora.getNome(), gravadora.getValor_contrato(), gravadora.getVencimento_contrato(), gravadora.created_at, gravadora.created_at)

        gravadora.setId(cursor.lastrowid)

        cursor.execute(sql, val)
        mydb.commit()

        return gravadora
    

    def update(artistas):
        cursor = mydb.getCursor()

        artistas.setUpdated_at(datetime.now())

        sql = "UPDATE artistas SET nome = %s, gravadoras_id = %s, updated_at = %s WHERE id = %s"
        val = (artistas.getNome(), artistas.getGravadoras_id(), datetime.now(), artistas.getId())

        cursor.execute(sql, val)
        mydb.commit()


        return artistas
    
    def remove(id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM artistas WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)
        mydb.commit()

        return True


