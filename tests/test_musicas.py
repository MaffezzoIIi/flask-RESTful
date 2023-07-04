import pytest

from src.models.Musicas import Musicas
from src.models.Generos import Generos
from datetime import datetime

def test_unit_musicas(mocker):
    # Cria um objeto Genero de exemplo
    exemplo_genero = Generos(
        id=1,
        descricao='Genero de teste',
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )

    # Cria um objeto Musica de exemplo
    exemplo_musica = Musicas(
        id=1,
        nome='Musica de teste',
        duracao=10,
        generos_id=exemplo_genero.id,
        lancamento=int(datetime.now().timestamp()),
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )
    
    mock_get = mocker.patch.object(Musicas.getId(exemplo_musica.id), 'get')
    mock_get.return_value = exemplo_musica
    
    musica = Musicas()
    
    musica_obtida = musica.get_musicas(1)
    
    mock_get.assert_called_once_with(1)

    assert musica_obtida.id == 1
    assert musica_obtida.nome == 'Musica de teste'