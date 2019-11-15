import json

def lista_de_usuarios(file):
    with open(file, 'r') as file:
        datos_usuario = json.load(file)
        lista_nombre_usuarios = datos_usuario
        for nombre_usuario in datos_usuario["nombre"]:
            lista_nombre_usuarios.append(nombre_usuario)
            with open('lista_usuarios.json', 'w') as file:
                json.dump(lista_nombre_usuarios, file)
                write_file('lista_usuarios.json', lista_nombre_usuarios)
    return file
