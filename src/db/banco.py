import mysql.connector

class Banco():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            database="mydb",
            user="milene",
            password="senha"
        )

    def getConexao(self):
        return self.mydb
    
    def getCursor(self):
        return self.mydb.cursor()
    
    def commit(self):
        self.mydb.commit()

