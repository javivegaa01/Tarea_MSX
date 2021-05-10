import os
import json
from flask import Flask, render_template,abort,request
app = Flask(__name__)	

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

@app.route('/juegos',methods=["GET","POST"])
def juegos():
    return render_template("juegos.html")

@app.route('/listajuegos',methods=["POST"])
def listajuegos():
    return render_template("listajuegos.html",juego=datos)
app.run(debug=True)