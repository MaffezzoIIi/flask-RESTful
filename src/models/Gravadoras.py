class Gravadorasa:

    def __init__(self, id, nome, valor_contrato, vencimento_contrato, created_at, updated_at):
        self.id = id
        self.nome = nome
        self.valor_contrato
        self.vencimento_contrato
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
