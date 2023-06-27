import pytest
from src.app import app, db, Generos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_create_genero(client):
    data = {
        'descricao': 'Genero de teste'
    }
    response = client.post('/api/generos', json=data)
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['descricao'] == data['descricao']


def test_get_genero(client):
    genero = Generos(descricao='Genero de teste', created_at=0, updated_at=0)
    db.session.add(genero)
    db.session.commit()
    response = client.get(f'/api/generos/{genero.id}')
    assert response.status_code == 200
    assert 'id' in response.json
    assert response.json['descricao'] == genero.descricao


def test_get_generos(client):
    genero1 = Generos(descricao='Genero 1', created_at=0, updated_at=0)
    genero2 = Generos(descricao='Genero 2', created_at=0, updated_at=0)
    db.session.add_all([genero1, genero2])
    db.session.commit()
    response = client.get('/api/generos')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.json[0]['descricao'] == genero1.descricao
    assert response.json[1]['descricao'] == genero2.descricao


def test_update_genero(client):
    genero = Generos(descricao='Genero de teste', created_at=0, updated_at=0)
    db.session.add(genero)
    db.session.commit()
    data = {
        'descricao': 'Novo genero'
    }
    response = client.put(f'/api/generos/{genero.id}', json=data)
    assert response.status_code == 200
    assert response.json['message'] == 'Genero atualizado com sucesso'
    assert response.json['Genero']['descricao'] == data['descricao']


if __name__ == '__main__':
    pytest.main()
