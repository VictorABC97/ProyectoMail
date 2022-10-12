from crypt import methods
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("login.html")

@app.route('/validarUsuario', methods=["GET","POST"])
def validarUsuario():
    if request.method=="POST":
        usuario = request.form["txtusuario"]
        passw = request.form["txtpass"]

        print("Usuario: " + usuario)
        print("Password: " + passw)
    return render_template("principal.html")