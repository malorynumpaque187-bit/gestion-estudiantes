import pytest
from app import app

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_listar_estudiantes(cliente):
    r = cliente.get('/students')
    assert r.status_code == 200

def test_crear_estudiante(cliente):
    payload = {
        "nombre": "Malory",
        "apellido": "Numpaque",
        "correo": "malory@correo.com"
    }
    r = cliente.post('/students', json=payload)
    assert r.status_code == 201

def test_salud(cliente):
    r = cliente.get('/salud')
    assert r.status_code == 200