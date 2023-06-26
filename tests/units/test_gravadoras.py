import pytest

from src.gravadora import Gravadora
from datetime import datetime, timedelta

def test_post_gravadora(mocker):
    #cria uma gravadora
    exemplo_gravadora = {
        'id': 1,
        'nome': 'Gravadora de teste',
        'valor_contrato': 99.99,
        'vencimento_contrato': int(datetime.now().timestamp()),
        'created_at'=int(datetime.now().timestamp() + timedelta(days=1)),
        'updated_at'=int(datetime.now().timestamp())
    }
