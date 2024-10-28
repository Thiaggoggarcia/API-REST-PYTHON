from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/about")
def about():
    return "About Python"   

if __name__ == "__main__":
    app.run(port=5001,debug=True)