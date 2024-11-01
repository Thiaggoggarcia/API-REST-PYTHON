from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Olá Mundo!"

@app.route("/sobre")
def sobre():
    return "Página Sobre"

@app.route("/tasks")
def task():
    return "Task"

if __name__ == "__main__":
    app.run(port= 5001,debug=True)
