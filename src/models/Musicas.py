class Musicas():

    def __init__(self, id, nome, duracao, generos_id, lancamento, created_at, updated_at):
        self.id = id
        self.nome = nome
        self.duracao = duracao
        self.generos_id = generos_id
        self.lancamento = lancamento
        self.created_at = created_at
        self.updated_at = updated_at

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getDuracao(self):
        return self.duracao

    def setDuracao(self, duracao):
        self.duracao = duracao

    def getGeneros_id(self):
        return self.generos_id

    def setGeneros_id(self, generos_id):
        self.generos_id = generos_id

    def getLancamento(self):
        return self.lancamento

    def setLancamento(self, lancamento):
        self.lancamento = lancamento

    def created_at(self):
        return self.created_at

    def setCreated_at(self, created_at):
        self.created_at = created_at

    def updated_at(self):
        return self.updated_at

    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at
