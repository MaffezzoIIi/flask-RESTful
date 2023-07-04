import pytest

from src.models.Artistas import Artistas
from src.models.Gravadoras import Gravadoras
from datetime import datetime

def test_unit_artistas(mocker):
    # Cria um objeto Artista de exemplo
    exemplo_gravadora = Gravadoras(
        id=1,
        nome='Gravadora de teste',
        valor_contrato=10,
        vencimento_contrato=int(datetime.now().timestamp())
    )

    exemplo_artista = Artistas(
        id=1,
        nome= "Artista de teste", 
        gravadoras_id = exemplo_gravadora.id
    )
    
    mock_get = mocker.patch.object(Artistas, 'getId')
    mock_get.return_value = exemplo_artista
    
    artista_obtido = exemplo_artista.getId(1)
    
    mock_get.assert_called_once_with(1)

    assert artista_obtido.id == 1
    assert artista_obtido.nome == 'Artista de teste'
