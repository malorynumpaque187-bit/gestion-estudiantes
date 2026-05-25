from flask import Flask, request, jsonify

app = Flask(__name__)

estudiantes = []
contador_id = 1

@app.route('/students', methods=['POST'])
def crear_estudiante():
    global contador_id
    datos = request.get_json()

    if not datos or 'nombre' not in datos or 'apellido' not in datos or 'correo' not in datos:
        return jsonify({'error': 'Faltan campos: nombre, apellido, correo'}), 400

    nuevo_estudiante = {
        'id': contador_id,
        'nombre': datos['nombre'],
        'apellido': datos['apellido'],
        'correo': datos['correo']
    }

    estudiantes.append(nuevo_estudiante)
    contador_id += 1

    return jsonify(nuevo_estudiante), 201

@app.route('/students/<int:id>', methods=['GET'])
def obtener_estudiante(id):
    for estudiante in estudiantes:
        if estudiante['id'] == id:
            return jsonify(estudiante), 200

    return jsonify({'error': 'Estudiante no encontrado'}), 404

@app.route('/students', methods=['GET'])
def listar_estudiantes():
    return jsonify(estudiantes), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)