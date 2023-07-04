import datetime
from src.db.banco import Banco

mydb = Banco()

class Gravadoras():

    def __init__(self, id, nome, valor_contrato, vencimento_contrato):
        self.id = id
        self.nome = nome
        self.valor_contrato = valor_contrato
        self.vencimento_contrato = vencimento_contrato
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

    def getValor_contrato(self):
        return self.valor_contrato

    def setValor_contrato(self, valor_contrato):
        self.valor_contrato = valor_contrato

    def getVencimento_contrato(self):
        return self.vencimento_contrato

    def setVencimento_contrato(self, vencimento_contrato):
        self.vencimento_contrato = vencimento_contrato

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

        sql = "INSERT INTO gravadoras (nome, valor_contrato, vencimento_contrato, created, modified) VALUES (%s, %s, %s, %s, %s)"
        val = (gravadora.getNome(), gravadora.getValor_contrato(), gravadora.getVencimento_contrato(), gravadora.created_at, gravadora.created_at)

        gravadora.setId(cursor.lastrowid)

        cursor.execute(sql, val)
        mydb.commit()

        return gravadora
    
    def getOne(id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM gravadoras WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)

        result = cursor.fetchone()
        
        gravadora =  Gravadoras(result[0], result[1], result[2], result[3])
        gravadora.setCreated_at(result[4])
        gravadora.setUpdated_at(result[5])
        return gravadora
    
    def getAll():
        cursor = mydb.getCursor()

        cursor.execute("SELECT * FROM gravadoras")
        myresult = cursor.fetchall()

        return myresult
    
    def update(gravadora, id):
        cursor = mydb.getCursor()

        sql = "UPDATE gravadoras SET nome = %s, valor_contrato = %s, vencimento_contrato = %s, modified = %s WHERE id = %s"
        val = (gravadora['nome'], gravadora['valor_contrato'], gravadora['vencimento_contrato'], datetime.datetime.now(), id)

        cursor.execute(sql, val)
        mydb.commit()

        select_query = "SELECT * FROM gravadoras WHERE id = %s"
        sql_val = (id,)
        cursor.execute(select_query, sql_val)
        result = cursor.fetchone()
        
        ngravadora =  Gravadoras(result[0], result[1], result[2], result[3])
        ngravadora.setCreated_at(result[4])
        ngravadora.setUpdated_at(result[5])
        
        return ngravadora
    
    def remove(id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM gravadoras WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)
        mydb.commit()

        return True
