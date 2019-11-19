from flask import Flask, request, jsonify
from persistence import update_from_front

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def enviar_datos():
    if request.method == 'POST':
        data = request.json
        update_from_front(data)
        result = update_from_front(data)
        return jsonify(result)

if __name__ == "__main__":
    app.run()
