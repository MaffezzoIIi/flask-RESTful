import pytest

from src.models.Pagamentos import Pagamentos
from datetime import datetime

def test_unit_pagamentos(mocker):
    # Cria um objeto Pagamento de exemplo
    dateNow = int(datetime.now().timestamp())
    exemplo_pagamento = Pagamentos(
        id=1,
        date=dateNow,
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )

    mock_get = mocker.patch.object(Pagamentos.getId(exemplo_pagamento.id), 'get')
    mock_get.return_value = exemplo_pagamento
    
    pagamento = Pagamentos()
    
    pagamento_obtido = pagamento.get_pagamentos(1)
    
    mock_get.assert_called_once_with(1)

    assert pagamento_obtido.id == 1
    assert pagamento_obtido.dateNow == int(datetime.now().timestamp())