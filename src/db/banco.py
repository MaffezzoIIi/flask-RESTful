import sqlite3

class Banco:

    def __init__(self):
        self.conexao = sqlite3.connect('./src/banco.db')
        self.createTables()

    def createTables(self):
        try:
            c = self.conexao.cursor()

            c.execute("""create table if not exists pagamentos (
                                 id integer primary key autoincrement,
                                 data INTEGER
                                 )""")
            self.conexao.commit()

            c.execute("""create table if not exists gravadoras (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    valor_contrato REAL NOT NULL,
                    vencimento_contrato INTEGER,
                    created_at INTEGER,
                    updated_at INTEGER
                )""")

            self.conexao.commit()

            c.execute("""create table if not exists planos (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL,
                    valor DECIMAL(5,2) NOT NULL,
                    limite INTEGER NOT NULL
                    created_at INTEGER,
                    updated_at INTEGER
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists generos (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT NOT NULL,
                    created_at INTEGER,
                    updated_at INTEGER
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists artistas (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    created_at INTEGER,
                    updated_at INTEGER,
                    gravadora_id INTEGER NOT NULL,
                    FOREIGN KEY(gravadora_id) REFERENCES gravadoras(id)
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists clientes (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    login TEXT NOT NULL,
                    senha TEXT NOT NULL,
                    created_at INTEGER,
                    updated_at INTEGER,
                    planos_id INTEGER NOT NULL,
                    FOREIGN KEY(planos_id) REFERENCES planos(id)
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists musicas (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    duracao INTEGER NOT NULL,
                    lancamento INTEGER,
                    created_at INTEGER,
                    updated_at INTEGER,
                    generos_id INTEGER NOT NULL,
                    FOREIGN KEY(generos_id) REFERENCES generos(id)
                )""")

            self.conexao.commit()

            print("Banco de dados ok")
            c.close()

        except sqlite3.Error as error:
            print("Erro ao conectar no SQLite", error)
