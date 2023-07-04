import datetime
from src.db.banco import Banco

mydb = Banco()

class Generos():

    def __init__(self, id, descricao, created_at, updated_at):
        self.id = id
        self.descricao = descricao
        self.created_at = created_at
        self.updated_at = updated_at

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
        val = (genero.getDescricao(), genero.created_at, genero.created_at)

        genero.setId(cursor.lastrowid)

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

        genero = Generos(result[0], result[1], result[2], result[3])

        return genero
    
    def getAll():
        cursor = mydb.getCursor()

        sql = "SELECT * FROM generos"

        cursor.execute(sql)

        result = cursor.fetchall()

        generos = []

        for row in result:
            genero = Generos(row[0], row[1], row[2], row[3])
            generos.append(genero)

        return generos
    
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