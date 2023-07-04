
import pytest

from datetime import datetime
from src.models.Gravadoras import Gravadoras

def test_unit_gravadoras(mocker):
    # Cria um objeto Gravadora de exemplo
    exemplo_gravadora = Gravadoras(
        id=1,
        nome='Gravadora de teste',
        valor_contrato=10,
        vencimento_contrato=int(datetime.now().timestamp()),
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )
    
    mock_get = mocker.patch.object(Gravadoras.getId(exemplo_gravadora.id), 'get')
    mock_get.return_value = exemplo_gravadora
    
    gravadora = Gravadoras()
    
    gravadora_obtida = gravadora.get_gravadoras(1)
    
    mock_get.assert_called_once_with(1)

    assert gravadora_obtida.id == 1
    assert gravadora_obtida.nome == 'Gravadora de teste'