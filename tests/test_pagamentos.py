import pytest

from src.models.Pagamentos import Pagamentos
from datetime import datetime

def test_unit_pagamentos(mocker):
    # Cria um objeto Pagamento de exemplo
    dateNow = int(datetime.now().timestamp())
    exemplo_pagamento = Pagamentos(
        id=1,
        date=dateNow,
    )

    mock_get = mocker.patch.object(Pagamentos, 'getId')
    mock_get.return_value = exemplo_pagamento
    
    pagamento_obtido = exemplo_pagamento.getId(1)
    
    mock_get.assert_called_once_with(1)

    assert pagamento_obtido.id == 1
    assert pagamento_obtido.date == int(datetime.now().timestamp())