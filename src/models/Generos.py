import datetime
from src.db.banco import Banco

mydb = Banco()

class Generos():

    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
        self.created_at = None
        self.updated_at = None

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getCreated_at(self):
        return self.created_at

    def setCreated_at(self, created_at):
        self.created_at = created_at

    def getUpdated_at(self):
        return self.updated_at

    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at

    def save(genero):
        cursor = mydb.getCursor()

        sql = "INSERT INTO generos (descricao, created, modified) VALUES (%s, %s, %s)"
        val = (genero.getDescricao(), datetime.datetime.now(), datetime.datetime.now())

        genero.setId(cursor.lastrowid)
        genero.setCreated_at(datetime.datetime.now())
        genero.setUpdated_at(datetime.datetime.now())

        cursor.execute(sql, val)
        mydb.commit()

        return genero
    
    def getOne(id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM generos WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)

        result = cursor.fetchone()

        if result is None:
            return None

        genero = Generos(result[0], result[1])
        genero.setCreated_at( result[2])
        genero.setUpdated_at(result[3])

        return genero
    
    def getAll():
        cursor = mydb.getCursor()

        sql = "SELECT * FROM generos"

        cursor.execute(sql)

        result = cursor.fetchall()
        
        return result
    
    def update(genero):
        cursor = mydb.getCursor()

        genero.updated_at = datetime.now()

        sql = "UPDATE generos SET descricao = %s, updated_at = %s WHERE id = %s"
        val = (genero.getDescricao(), genero.updated_at, genero.getId())

        cursor.execute(sql, val)
        mydb.commit()

        return genero
    
    def remove(id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM generos WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)
        mydb.commit()

        return True