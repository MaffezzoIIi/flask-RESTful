class Planos():
    
    def __init__(self, id_plano, nome_plano, valor_plano, descricao_plano):
        self.id_plano = id_plano
        self.nome_plano = nome_plano
        self.valor_plano = valor_plano
        self.descricao_plano = descricao_plano
        self.created_at = None
        self.updated_at = None

    def getId_plano(self):
        return self.id_plano

    def setId_plano(self, id_plano):
        self.id_plano = id_plano

    def getNome_plano(self):
        return self.nome_plano

    def setNome_plano(self, nome_plano):
        self.nome_plano = nome_plano

    def getValor_plano(self):
        return self.valor_plano

    def setValor_plano(self, valor_plano):
        self.valor_plano = valor_plano

    def getDescricao_plano(self):
        return self.descricao_plano

    def setDescricao_plano(self, descricao_plano):
        self.descricao_plano = descricao_plano
        
    def getCreated_at(self):
        return self.created_at
        
    def setCreated_at(self, created_at):
        self.created_at = created_at
        
    def getUpdated_at(self):
        return self.updated_at
        
    def setUpdated_at(self, updated_at):
        self.updated_at = updated_at