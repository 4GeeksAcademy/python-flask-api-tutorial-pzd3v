from flask import Flask,jsonify,request

app = Flask(__name__)

# asegúrate de convertir el cuerpo de la solicitud en una estructura de datos real de Python, como un diccionario.  Ya usamos request.json para eso, ya que sabemos que la solicitud estará en formato application/json. Si el formato no se conoce, es posible que deba usar request.get_json(force=True) para ignorar el tipo de contenido y tratarlo como json.
todos = [ 
   { "label": "My first task", "done": False } ]

@app.route("/todos",methods=["GET"])
def get_todos():
    jason_text = jsonify(todos)
    return jason_text

@app.route("/todos",methods=["POST"])
def add_new_todo():
   request_body = request.get_json(force=True)
   print("Incoming request with the following body", request_body)
   todos.append(request_body)
   return jsonify(todos)

@app.route("/todos/<int:position>",methods=["DELETE"])
def delete_todo(position):
   print("This is the position to delete:",position)
   todos.pop(position)
   return jsonify(todos)

#Estas lineas siempre deben estar al final del archivo app.py
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3245,debug=True)