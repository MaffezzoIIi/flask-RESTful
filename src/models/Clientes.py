class Clientes():

    def __init__(self, id, login, senha, email, planos_id, created_at, updated_at):
        self.id = id
        self.login = login
        self.senha = senha
        self.email = email
        self.planos_id = planos_id
        self.created_at = created_at
        self.updated_at = updated_at

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
