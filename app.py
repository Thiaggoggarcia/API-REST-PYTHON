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
    return jsonify({"Mensagem": "Nova tarefa criada com sucesso!"})


@app.route("/tasks", methods=['GET'])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict()) 
    
    total_tasks = len(task_list)
    output = {
        "tasks":task_list,
        "total_tasks": total_tasks
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(port=5001,debug=True)
    
    
    