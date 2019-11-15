from flask import Flask, request, jsonify
from funciones_post import comprobar_existe_usuario
from funciones_get import lista_de_usuarios

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def enviar_datos(nombre_usuario):
    if request.method == 'POST':
        data = request.json
        return(comprobar_existe_usuario(data, nombre_usuario))

    if request.method == 'GET':
        data = request.json
        lista_de_usuarios(data)
        return data


if __name__ == "__main__":
    app.run()

