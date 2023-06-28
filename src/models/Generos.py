class Generos():

    def __init__(self, id, descricao, created_at, updated_at):
        self.id = id
        self.descricao = descricao
        self.created_at = created_at
        self.updated_at = updated_at

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getDescricao(self):
        return self.descricao

    def setDescricao(self, descricao):
        self.descricao = descricao

    def getCreated_at(self):
        return self.created_at

    def setCreated_at(self, created_at):
        self.created_at = created_at

    def getUpdated_at(self):
        return self.updated_at

    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at
