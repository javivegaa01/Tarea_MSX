import os
import json
from flask import Flask, render_template,abort,request
app = Flask(__name__)	

with open("MSX.json") as fichero:
    datos=json.load(fichero)

@app.route('/',methods=["GET"])
def inicio():
	return render_template("inicio.html")

app.run(debug=True)