# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Olá, Mundo! Meu projeto DevOps está no ar!</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
