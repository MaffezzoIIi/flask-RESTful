import pytest

from src.models.Clientes import Clientes
from src.models.Planos import Planos

def test_unit_clientes(mocker):
    # Cria um objeto Plano de exemplo
    exemplo_plano = Planos(
        id=1,
        valor=10,
        descricao='Plano de teste',
        limite=10
    )

    exemplo_cliente = Clientes(
        id=1,
        login='Cliente de teste',
        senha='123456',
        email='cliente@gmail.com',
        planos_id=exemplo_plano.id
    )

    mock_get = mocker.patch.object(Clientes, 'getId')
    mock_get.return_value = exemplo_cliente

    cliente_obtido = exemplo_cliente.getId(1)

    mock_get.assert_called_once_with(1)

    assert cliente_obtido.id == 1
    assert cliente_obtido.login == 'Cliente de teste'
    

