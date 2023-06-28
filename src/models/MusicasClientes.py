class MusicasClientes():

    def __init__(self, musica_id, clientes_id):
        self.musica_id = musica_id
        self.clientes_id = clientes_id

    def getMusica_id(self):
        return self.musica_id

    def setMusica_id(self, musica_id):
        self.musica_id = musica_id

    def getClientes_id(self):
        return self.clientes_id

    def setClientes_id(self, clientes_id):
        self.clientes_id = clientes_id
