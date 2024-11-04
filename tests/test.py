#import pytest
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
    tasks.append(json_response['id'])

def test_get_task():
    resposta = requests.get(f"{BASE_URL}/tasks")
    assert resposta.status_code == 200
    resposta_json = resposta.json()
    assert "tasks" in resposta_json
    assert "total_tasks" in resposta_json

def test_get_task_unique():
    for task in tasks:
        resposta = requests.get(f"{BASE_URL}/tasks/{task}")
        resposta_json = resposta.json()
        assert resposta.status_code == 200
        assert task == resposta_json['id']

def test_updade_task():
    update_task = {
        'title': 'Atualizando Atividade',
        'description': 'Atualizando Atividade já Cadastrada!',
        'completed': True
        
    }
    task_id = tasks[0]
    resposta = requests.put(f"{BASE_URL}/tasks/{task_id}",json=update_task)
    assert resposta.status_code == 200
    assert 'Mensagem' in resposta.json()
    
def test_delete_task():
  
    resposta = requests.delete(f"{BASE_URL}/tasks/{tasks[0]}")
    resposta.status_code == 200
        
    resposta2 = requests.get(f"{BASE_URL}/tasks/{tasks[0]}")
    assert resposta2.status_code == 404
   
    