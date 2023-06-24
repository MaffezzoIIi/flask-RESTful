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
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    valor_contrato REAL,
                    vencimento_contrato INTEGER,
                    created_at INTEGER,
                    updated_at INTEGER
                )""")

            self.conexao.commit()

            c.execute("""create table if not exists planos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT,
                    valor DECIMAL(5,2),
                    limite INTEGER
                    created_at INTEGER,
                    updated_at INTEGER
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists generos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    descricao TEXT,
                    created_at INTEGER,
                    updated_at INTEGER
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists artistas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    created_at INTEGER,
                    updated_at INTEGER,
                    gravadora_id INTEGER,
                    FOREIGN KEY(gravadora_id) REFERENCES gravadoras(id)
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT,
                    senha TEXT,
                    created_at INTEGER,
                    updated_at INTEGER,
                    planos_id INTEGER,
                    FOREIGN KEY(planos_id) REFERENCES planos(id)
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists musicas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    duracao INTEGER,
                    lancamento INTEGER,
                    created_at INTEGER,
                    updated_at INTEGER,
                    generos_id INTEGER,
                    FOREIGN KEY(generos_id) REFERENCES generos(id)
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists musicas_has_artistas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    musicas_id INTEGER,
                    artistas_id INTEGER,
                    FOREIGN KEY(musicas_id) REFERENCES musicas(id),
                    FOREIGN KEY(artistas_id) REFERENCES artistas(id)
                )""")

            self.conexao.commit()

            c.execute(""" create table if not exists musicas_has_clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    musicas_id INTEGER,
                    clientes_id INTEGER,
                    FOREIGN KEY(musicas_id) REFERENCES musicas(id),
                    FOREIGN KEY(clientes_id) REFERENCES clientes(id)
                )""")

            self.conexao.commit()

            print("Banco de dados ok")
            c.close()

        except sqlite3.Error as error:
            print("Erro ao conectar no SQLite", error)
