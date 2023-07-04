from src.db.banco import Banco
from datetime import datetime

mydb = Banco()

class Planos():
    
    def __init__(self, id, valor, descricao, limite):
        self.id = id
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

        sql = "INSERT INTO planos (descricao, valor, limite, created, modified) VALUES (%s, %s, %s, %s, %s)"
        val = (plano.getDescricao(), plano.getValor(), plano.getLimite(), plano.created_at, plano.created_at)

        plano.setId(cursor.lastrowid)

        cursor.execute(sql, val)
        mydb.commit()

        return plano
    
    def getAll():
        cursor = mydb.getCursor()

        cursor.execute("SELECT * FROM planos")
        myresult = cursor.fetchall()

        return myresult

    def getOne(id):
        cursor = mydb.getCursor()

        cursor.execute("SELECT * FROM planos WHERE id = %s", (id,))

        myresult = cursor.fetchone()

        plano =  Planos(myresult[0], myresult[1], myresult[2], myresult[3])
        plano.setCreated_at(myresult[4])
        plano.setUpdated_at(myresult[5])
        return plano
    
    def update(newData, id):
        cursor = mydb.getCursor()

        sql = "UPDATE planos SET descricao = %s, valor = %s, limite = %s, modified = %s WHERE id = %s"
        val = (newData['descricao'], newData['valor_plano'], newData['limite'], datetime.now(), id)

        cursor.execute(sql, val)
        mydb.commit()
        
        return Planos.getOne(id)
    
    def remove(id):
        cursor = mydb.getCursor()

        cursor.execute("DELETE FROM planos WHERE id = %s", (id,))

        mydb.commit()

        return True
        
    
        