from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
id_control = 1 

@app.route("/tasks", methods=["POST"])
def create():
    global id_control
    data = request.get_json()
    new_task = Task(id=id_control, title=data["title"], description=data["description"], completed=data["completed"])
    id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso."})

if __name__ == "__main__":
    app.run(debug=True)