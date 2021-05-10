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
    return render_template("juegos.html",juego=datos)

@app.route('/listajuegos',methods=["POST"])
def listajuegos():
    lista_juegos=[]
    cad=request.form.get("search_control")
    if cad!=" ":
        for a in datos:
            if str(a["nombre"]).startswith(cad):
                lista_juegos.append(str(a["nombre"]))
    else:
        for a in datos:
            lista_juegos.append(str(a["nombre"]))
    return render_template("listajuegos.html",lista_juegos=set(lista_juegos))

app.run(debug=True)