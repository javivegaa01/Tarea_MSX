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
    if request.method == "GET":
        lista_categoria=[]
        for juegos in datos:
            lista_categoria.append(juegos["categoria"])
        return render_template('juegos.html', lista_categoria=set(lista_categoria))
    else:
        nombre_juego=request.form.get("nombre")
        categoria=request.form.get("categorias")
        lista_nombres=[]
        lista_desarrolladores=[]
        lista_ids=[]
        lista_categoria=[]
        for juegos in datos:
            lista_categoria.append(juegos["categoria"])
            if nombre_juego == "" and str(juegos["categoria"]) == categoria:
                lista_desarrolladores.append(juegos["desarrollador"])
                lista_nombres.append(juegos["nombre"])
                lista_ids.append(juegos["id"])
            elif str(juegos["nombre"]).startswith(nombre_juego) and str(juegos["categoria"]) == categoria:
                lista_desarrolladores.append(juegos["desarrollador"])
                lista_nombres.append(juegos["nombre"])
                lista_ids.append(juegos["id"])
        return render_template("juegos.html", nombre_juego=nombre_juego, lista_nombres=lista_nombres, lista_desarrolladores=lista_desarrolladores, lista_ids=lista_ids, lista_categoria=set(lista_categoria))

@app.route('/juego/<int:identificador>')
def juego_id(identificador):
    for juegos in datos:
        if juegos["id"] == identificador:
            return render_template('idjuegos.html', juego=juegos)
        
    return abort(404)


app.run(debug=True)