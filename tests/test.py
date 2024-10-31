import pytest
import requests

BASE_URL = 'http://127.0.0.1:5001'
tasks = []

def test_create_task():
    new_task = {
        'title': 'Nova Atividade',
        'description': 'Adicionando nova Atividade'
    }
    
    resposta = requests.post(f"{BASE_URL}/tasks",json=new_task)
    assert resposta.status_code == 200
    json_response = resposta.json()
    assert "Mensagem" in json_response
    assert "id" in json_response