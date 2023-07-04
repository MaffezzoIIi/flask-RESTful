import pytest

from src.models.Musicas import Musicas
from src.models.Generos import Generos
from datetime import datetime

def test_unit_musicas(mocker):
    # Cria um objeto Genero de exemplo
    exemplo_genero = Generos(
        id=1,
        descricao='Genero de teste'
    )

    # Cria um objeto Musica de exemplo
    exemplo_musica = Musicas(
        id=1,
        nome='Musica de teste',
        duracao=10,
        generos_id=exemplo_genero.id,
        lancamento=int(datetime.now().timestamp())
    )
    
    mock_get = mocker.patch.object(Musicas, 'getId')
    mock_get.return_value = exemplo_musica
    
    musica_obtida = exemplo_musica.getId(1)
    
    mock_get.assert_called_once_with(1)

    assert musica_obtida.id == 1
    assert musica_obtida.nome == 'Musica de teste'