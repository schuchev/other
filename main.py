from flask import Flask, jsonify, request, abort

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Flask", "description": "Study Flask framework"},
    {"id": 2, "title": "Build a REST API", "description": "Create a simple REST API"}
]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    found_tasks = [t for t in tasks if t["id"] == task_id]
    task = found_tasks[0] if found_tasks else None
    return jsonify(task)


@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        "id": tasks[-1]["id"] + 1 if tasks else 1,
        "title": request.json["title"],
        "description": request.json["description"]
    }
    tasks.append(new_task)
    return jsonify(new_task),201



@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    found_tasks = [t for t in tasks if t["id"] == task_id]
    task = found_tasks[0] if found_tasks else None
    task["title"] = request.json.get("title", task["title"])
    task["description"] = request.json.get("description", task["description"])

    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    found_tasks = [t for t in tasks if t["id"] == task_id]
    task = found_tasks[0] if found_tasks else None
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"result": True})


if __name__ == '__main__':
    app.run(debug=True)
