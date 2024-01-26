import json
import pytest
import os
import sys
from application_flask.app import lire_jsonl
from application_flask.app import app

# Ajout du répertoire parent au PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Fixture pour créer un fichier .jsonl temporaire
@pytest.fixture
def mock_jsonl(tmp_path):
    data = [{"id": 1, "text": "Test 1"}, {"id": 2, "text": "Test 2"}]
    temp_file = tmp_path / "temp.jsonl"
    with open(temp_file, 'w') as file:
        for item in data:
            file.write(json.dumps(item) + '\n')
    return str(temp_file)

# Fonction de test
def test_lire_jsonl(mock_jsonl):
    resultats = list(lire_jsonl(mock_jsonl))
    assert len(resultats) == 2  # Vérifie que deux éléments sont lus
    assert resultats[0]['id'] == 1  # Vérifie que le premier élément est correct
    assert resultats[1]['id'] == 2  # Vérifie que le deuxième élément est correct

@pytest.fixture
def empty_jsonl(tmp_path):
    temp_file = tmp_path / "empty.jsonl"
    temp_file.touch()  # Crée un fichier vide
    return str(temp_file)

@pytest.fixture
def bad_jsonl(tmp_path):
    temp_file = tmp_path / "bad.jsonl"
    with open(temp_file, 'w') as file:
        file.write('{"id": 1, "text": "Test 1"')  # Données JSON mal formées
    return str(temp_file)

def test_lire_jsonl_with_empty_file(empty_jsonl):
    resultats = list(lire_jsonl(empty_jsonl))
    assert len(resultats) == 0  # Doit retourner une liste vide

def test_lire_jsonl_with_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        list(lire_jsonl('nonexistent.jsonl'))  # Doit lever une FileNotFoundError

def test_lire_jsonl_with_bad_data(bad_jsonl):
    with pytest.raises(json.JSONDecodeError):
        list(lire_jsonl(bad_jsonl))  # Doit lever une JSONDecodeError car les données sont mal formées

# Fixture pour configurer le client de test Flask
@pytest.fixture
def client():
    # Définir ici le chemin absolu vers le fichier 'resultats.jsonl'
    app.config['TESTING'] = True
    resultats_path = os.path.join(app.root_path, 'data', 'resultats.jsonl')
    print(resultats_path)
    app.config['RESULTATS_JSONL_PATH'] = resultats_path

    with app.test_client() as client:
        yield client

# Test pour la route qui retourne un item aléatoire
def test_get_random_item(client):
    # Assurez-vous que votre logique d'application utilise app.config['RESULTATS_JSONL_PATH']
    # pour localiser le fichier 'resultats.jsonl'
    response = client.get('/')
    assert response.status_code == 200
    # Effectuer des assertions supplémentaires sur le contenu si nécessaire
