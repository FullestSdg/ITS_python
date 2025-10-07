from flask import Flask 

app2 = Flask(__name__)

@app2.route("/about")
def route() -> str:
    return "<h1> Viva l'esdrongo! </h1>"

@app2.route("/user/<nome>")
def nome(nome:str) -> str:
    return f"Benvenuto, {nome}!"

@app2.route("/square/<int:n>")
def square(n:int) -> int:
    return f"Il quadrato di {n} è {n ** 2}"

@app2.route("/sum/<int:a>/<int:b>")
def sum(a:int, b:int) -> int:
    return f"La somma è {a+b}"