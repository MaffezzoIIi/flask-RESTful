# import pytest
# from app import app, db

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         with app.app_context():
#             db.create_all()
#         yield client
#         with app.app_context():
#             db.drop_all()

# def test_create_genero(client):
#     data = {
#         'descricao': 'Genero de teste'
#     }
#     response = client.post('/api/generos', json=data)
#     assert response.status_code == 201
#     assert 'id' in response.json
#     assert response.json['descricao'] == data['descricao']
