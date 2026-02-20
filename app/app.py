from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker – DevOps Task-10, DevOps pipeline around a containerized application"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

