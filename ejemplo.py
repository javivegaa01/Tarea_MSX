import json
with open("MSX.json") as fichero:
    datos=json.load(fichero)

for a in datos:
    print(a["nombre"])