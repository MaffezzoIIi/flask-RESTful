import sqlite3

class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('db/banco.db')
        self.createTables()

    def createTables(self):
        try:
            c = self.conexao.cursor()

            c.execute("""create table if not exists funcionarios (
                                 id_funcionario integer primary key autoincrement,
                                 nome text not null,
                                 sexo text,
                                 data_nascimento text,
                                 qtd_dependentes integer,
                                 cargo text,
                                 salario integer,
                                 id_setor integer)""")
            self.conexao.commit()
            print("Banco de dados ok")
            c.close()

        except sqlite3.Error as error:
            print("Erro ao conectar no SQLite", error)