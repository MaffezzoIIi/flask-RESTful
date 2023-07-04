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
        vencimento_contrato=int(datetime.now().timestamp()),
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )

    exemplo_artista = Artistas(
        id=1,
        nome= "Artista de teste", 
        gravadoras_id = exemplo_gravadora.id,
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )
    
    mock_get = mocker.patch.object(Artistas.getId(exemplo_artista.id), 'get')
    mock_get.return_value = exemplo_artista
    
    artista = Artistas()
    
    artista_obtido = artista.get_artistas(1)
    
    mock_get.assert_called_once_with(1)

    assert artista_obtido.id == 1
    assert artista_obtido.nome == 'Artista de teste'
