import datetime
from src.db.banco import Banco

mydb = Banco()

class Artistas():

    def __init__(self, id, nome, gravadoras_id):
        self.id = id
        self.nome = nome
        self.gravadoras_id = gravadoras_id
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

    def save(artistas):
        cursor = mydb.getCursor()

        sql = "INSERT INTO artistas (nome, gravadoras_id, created, modified) VALUES (%s, %s, %s, %s)"
        val = (artistas.getNome(), artistas.getGravadoras_id(), artistas.getCreated_at(), artistas.getCreated_at())

        artistas.setId(cursor.lastrowid)

        cursor.execute(sql, val)
        mydb.commit()

        return artistas
    

    def update(artistas, id):
        cursor = mydb.getCursor()

        sql = "UPDATE artistas SET nome = %s, gravadoras_id = %s, modified = %s WHERE id = %s"
        val = (artistas['nome'], artistas['gravadoras_id'], datetime.datetime.now(), id)

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
    
    def getAll():
        cursor = mydb.getCursor()
        
        sql = "SELECT * FROM artistas"

        cursor.execute(sql)

        result = cursor.fetchall()
        
        return result
    
    def getOne(id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM artistas WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)

        result = cursor.fetchone()
        return result

