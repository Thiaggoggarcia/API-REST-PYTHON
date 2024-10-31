from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)
task_id_control = 1
tasks = []

@app.route("/tasks", methods=['POST'])
def create_tasks():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control ,title=data["title"], description=data.get("description",""))
    tasks.append(new_task)
    task_id_control += 1
    return jsonify({"Mensagem": "Nova tarefa criada com sucesso!", "id":new_task.id})


@app.route("/tasks", methods=['GET'])
def get_tasks():
    
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks":task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id_task>", methods=['GET'])
def get_id_task(id_task):
    if tasks == []:
        return jsonify({'Mensagem': 'Não Existem Atividades Cadastradas!'}), 404
    
    for task in tasks:
        if task.id == id_task:
            return task.to_dict()

        return jsonify({"Mensagem": "Atividade Não encontrada!"}), 404
    
@app.route("/tasks/<int:taskId>", methods=['PUT'])
def update_task(taskId):
    if tasks == []:
        return jsonify({'Mensagem': 'Não Existem Atividades Cadastradas!'}), 404
    
    for task in tasks:
        print(task.id,type(task.id))
        if task.id == taskId:
            data = request.get_json()
            task.title = data['title']
            task.description = data['description']
            task.completed = data['completed']
            return jsonify({'Mensagem': 'Atividade Atualizada com Sucesso!'})
        
        return jsonify({"Mensagem": "Atividade Não encontrada!"}), 404
            
@app.route("/tasks/<int:id_task>", methods=['DELETE'])
def delete_task(id_task):
    if tasks == []:
        return jsonify({'Mensagem': 'Não Existem Atividades Cadastradas!'}), 404
    
    for task in tasks:
        if task.id == id_task:
            print(task)
            tasks.remove(task)
            return jsonify({"Mensagem": "Atividade Deletada com Sucesso!"})
        
        return jsonify({"Mensagem": "Atividade Não encontrada!"}), 404


if __name__ == "__main__":
    app.run(port=5001,debug=True)
    
    
    