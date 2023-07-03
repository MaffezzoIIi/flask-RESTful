import datetime
from src.db.banco import Banco

mydb = Banco()

class Planos():
    
    def __init__(self, valor, descricao, limite):
        self.id = None
        self.valor = valor
        self.descricao = descricao
        self.limite = limite
        self.created_at = None
        self.updated_at = None

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getLimite(self):
        return self.limite
    
    def setLimite(self, limite):
        self.limite = limite
        
    def getCreated_at(self):
        return self.created_at
        
    def setCreated_at(self, created_at):
        self.created_at = created_at
        
    def getUpdated_at(self):
        return self.updated_at
        
    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at

    def save(plano):
        cursor = mydb.getCursor()


        sql = "INSERT INTO customers (descricao, valor, limte, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
        val = (plano.getDescricao(), plano.getValor(), plano.getLimite(), plano.created_at, plano.created_at)

        plano.setId(cursor.lastrowid)

        cursor.execute(sql, val)
        mydb.commit()

        return plano
    
    def getAll():
        cursor = mydb.getCursor()

        cursor.execute("SELECT * FROM planos")
        myresult = cursor.fetchall()

        for x in myresult:
            print(x)

        return myresult

    def getOne(id):
        cursor = mydb.getCursor()

        cursor.execute("SELECT * FROM planos WHERE id = %s", (id,))

        myresult = cursor.fetchone()

        return myresult
    
    def update(newData):
        cursor = mydb.getCursor()

        sql = "UPDATE planos SET descricao = %s, valor = %s, limite = %s, updated_at = %s WHERE id = %s"
        val = (newData.getDescricao(), newData.getValor(), newData.getLimite(), newData.updated_at, newData.getId())

        cursor.execute(sql, val)
        mydb.commit()

        return newData
    
    def remove(id):
        cursor = mydb.getCursor()

        cursor.execute("DELETE FROM planos WHERE id = %s", (id,))

        mydb.commit()

        return True
        
    
        