# Importamos Flask para el servidor, jsonify para responder en JSON y request para leer lo que envía el cliente
from flask import Flask, jsonify, request

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Nuestra "Base de Datos" temporal (una lista de diccionarios en memoria)
todos = [
    { "label": "My first task", "done": False } 
]

# --- RUTA PARA OBTENER TAREAS (READ) ---
@app.route("/todos", methods=["GET"])
def get_todos():
    # Convertimos la lista de Python a un formato JSON que el navegador entienda
    return jsonify(todos)

# --- RUTA PARA AÑADIR UNA TAREA (CREATE) ---
@app.route("/todos", methods=["POST"])
def add_new_todo():
    # Extraemos el cuerpo de la solicitud (el JSON que envía el cliente)
    # force=True asegura que intente leerlo como JSON aunque el header no sea perfecto
    request_body = request.get_json(force=True)
    
    print("Incoming request with the following body", request_body)
    
    # Añadimos el nuevo diccionario a nuestra lista 'todos'
    todos.append(request_body)
    
    # Devolvemos la lista actualizada para confirmar que se guardó
    return jsonify(todos)

# --- RUTA PARA ELIMINAR UNA TAREA (DELETE) ---
# Usamos <int:position> para capturar un número desde la URL (ej: /todos/0)
@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    # Eliminamos el elemento en el índice indicado usando el método .pop() de las listas
    todos.pop(position)
    
    # Devolvemos la lista restante
    return jsonify(todos)

# --- CONFIGURACIÓN DEL SERVIDOR ---
if __name__ == "__main__":
    # Ejecutamos el servidor en el puerto 3245
    # host="0.0.0.0" permite que sea accesible desde fuera de tu red local
    # debug=True reinicia el servidor automáticamente cuando guardas cambios
    app.run(host="0.0.0.0", port=3245, debug=True)
