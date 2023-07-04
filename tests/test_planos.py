import pytest

from datetime import datetime
from src.models.Planos import Planos

def test_unit_planos(mocker):
    # Cria um objeto Plano de exemplo
    exemplo_plano = Planos(
        id=1,
        valor=10,
        descricao='Plano de teste',
        limite=10
    )
    
    mock_get = mocker.patch.object(Planos, 'getId')
    mock_get.return_value = exemplo_plano
    
    plano_obtido = exemplo_plano.getId(1)
    
    mock_get.assert_called_once_with(1)

    assert plano_obtido.id == 1
    assert plano_obtido.valor == 10
    assert plano_obtido.descricao == 'Plano de teste'
    assert plano_obtido.limite == 10