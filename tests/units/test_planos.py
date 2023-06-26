import pytest

from src.models.Planos import Planos
from datetime import datetime

def test_get_planos(mocker):
    # Cria um objeto Plano de exemplo
    exemplo_plano = Planos(
        id=1,
        descricao='Plano de teste',
        valor=99.99,
        limite=100,
        created_at=int(datetime.now().timestamp()),
        updated_at=int(datetime.now().timestamp())
    )
    
    mock_get = mocker.patch.object(Planos.query, 'get')
    mock_get.return_value = exemplo_plano
    
    plano = Planos()
    
    plano_obtido = plano.get_planos(1)
    
    mock_get.assert_called_once_with(1)

    assert plano_obtido.id == 1
    assert plano_obtido.descricao == 'Plano de teste'
    assert plano_obtido.valor == 99.99
    assert plano_obtido.limite == 100

    def test_alterar_plano(mocker):
      exemplo_plano = Planos(
          id=1,
          descricao='Plano de teste',
          valor=99.99,
          limite=100,
          created_at=int(datetime.now().timestamp()),
          updated_at=int(datetime.now().timestamp())
      )
      
      mocker.patch.object(Planos, 'get_plano', return_value=exemplo_plano)
      
      mocker.patch.object(Planos, 'commit')
      
      plano = Planos()
      
      plano.alterar_plano(1, 'Plano atualizado', 149.99, 200)
      
      Planos.get_plano.assert_called_once_with(1)
      
      assert exemplo_plano.descricao == 'Plano atualizado'
      assert exemplo_plano.valor == 149.99
      assert exemplo_plano.limite == 200
      
      Planos.commit.assert_called_once()