class Artistas():

    def __init__(self, id, nome, gravadoras_id, created_at, updated_at):
        self.id = id
        self.nome = nome
        self.gravadoras_id = gravadoras_id
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

    def getGravadoras_id(self):
        return self.gravadoras_id

    def setGravadoras_id(self, gravadoras_id):
        self.gravadoras_id = gravadoras_id

    def getCreated_at(self):
        return self.created_at

    def setCreated_at(self, created_at):
        self.created_at = created_at

    def getUpdated_at(self):
        return self.updated_at

    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at
