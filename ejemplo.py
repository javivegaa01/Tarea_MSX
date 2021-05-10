import json
with open("MSX.json") as fichero:
    datos=json.load(fichero)

a=input("juego: ")

for juegos in datos:
    if str(juegos["nombre"]).startswith(a):
        print(juegos["nombre"])


