import pytest

from src.models.Generos import Generos
from datetime import datetime

def test_unit_generos(mocker):
    # Cria um objeto Genero de exemplo
    exemplo_genero = Generos(
        id=1,
        descricao='Genero de teste',
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )

    mock_get = mocker.patch.object(Generos.getId(exemplo_genero.id), 'get')
    mock_get.return_value = exemplo_genero
    
    genero = Generos()
    
    genero_obtido = genero.get_generos(1)
    
    mock_get.assert_called_once_with(1)

    assert genero_obtido.id == 1
    assert genero_obtido.descricao == 'Genero de teste'