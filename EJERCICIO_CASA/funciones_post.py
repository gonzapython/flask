import json

def comprobar_existe_usuario(file, nombre):
    with open(file, 'r') as file:
        datos_usuario = json.load(file)
        if datos_usuario["nombre"] == nombre:
            return "Ya existe el usuario"
