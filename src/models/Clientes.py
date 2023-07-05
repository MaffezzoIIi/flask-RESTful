import datetime
from src.db.banco import Banco

mydb = Banco()

class Clientes():

    def __init__(self, id, login, senha, email, planos_id):
        self.id = id
        self.login = login
        self.senha = senha
        self.email = email
        self.planos_id = planos_id
        self.created_at = None
        self.updated_at = None

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getLogin(self):
        return self.login

    def setLogin(self, login):
        self.login = login

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPlanos_id(self):
        return self.planos_id

    def setPlanos_id(self, planos_id):
        self.planos_id = planos_id

    def getCreated_at(self):
        return self.created_at

    def setCreated_at(self, created_at):
        self.created_at = created_at

    def getUpdated_at(self):
        return self.updated_at

    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at

    def save(cliente):
        cursor = mydb.getCursor()

        sql = "INSERT INTO clientes (login, senha, email, planos_id, created, modified) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (cliente.getLogin(), cliente.getSenha(), cliente.getEmail(), cliente.getPlanos_id(), cliente.created_at, cliente.created_at)

        cliente.setId(cursor.lastrowid)

        cursor.execute(sql, val)
        mydb.commit()

        return cliente
    
    def getOne(id):
        cursor = mydb.getCursor()

        sql = "SELECT * FROM clientes WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)

        result = cursor.fetchone()

        return result
    
    def getAll():
        cursor = mydb.getCursor()

        cursor.execute("SELECT * FROM clientes")
        myresult = cursor.fetchall()

        return myresult
    
    def update(cliente, id):

        cursor = mydb.getCursor()

        sql = "UPDATE clientes SET login = %s, senha = %s, email = %s, planos_id = %s, modified = %s WHERE id = %s"
        val = (cliente['login'], cliente['senha'], cliente['email'], cliente['planos_id'],  datetime.datetime.now(), id)

        cliente['updated_at'] = datetime.datetime.now()

        cursor.execute(sql, val)
        mydb.commit()

        return cliente
    
    def remove(id):
        cursor = mydb.getCursor()

        sql = "DELETE FROM clientes WHERE id = %s"
        val = (id, )

        cursor.execute(sql, val)
        mydb.commit()

        return True
    
