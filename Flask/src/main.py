#   Importaciones de Paquetes Flask
from flask import Flask, jsonify, request, Response
from flask import render_template
from flask_pymongo import PyMongo, ObjectId
from decouple import config
from werkzeug.security import generate_password_hash
from bson import json_util
from bson.objectid import ObjectId

#   Configuracion Inicial de Flas
app = Flask(__name__)
#   Conexion a MongoDB
app.config['MONGO_URI'] = config("MONGOCDN")
mongo = PyMongo(app)


#   Rutas
@app.route('/')
def index():
    return "Aprendiendo Flask con Master en Python <h1> Home Page</h1>"

@app.route('/usuarios', methods = ['POST'])
def create_user():
    #   Reciving Data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if username and email and password:
        has_pass = generate_password_hash(password)
        id = mongo.db.usuarios.insert_one({"username" : username, "email" : email, "password" : has_pass})
        response = {
            "username" : username,
            "password" : has_pass,
            "email" : email,
        }
        back = json_util.dumps(response)
        return Response(back, mimetype="application/json")
    else:
        return page_not_found()

@app.route('/usuarios', methods= ['GET'])
def get_users():
    usuarios = mongo.db.usuarios.find({})
    response = json_util.dumps(usuarios)
    return Response(response, mimetype="application/json")

@app.route("/usuarios/<id>", methods=['GET'])
def get_user(id):
    usuario = mongo.db.usuarios.find_one({'_id' : ObjectId(id)})
    response = json_util.dumps(usuario)
    return Response(response, mimetype="application/json")

@app.route("/usuarios/<id>", methods=['DELETE'])
def delete_user(id):
    usuario = mongo.db.usuarios.delete_one({'_id' : ObjectId(id)})
    message =  jsonify({'message' : f"Usuario con ID: {id} Fue eliminado Correctamente "})
    return message



@app.route('/usuarios/<id>', methods=['PUT'])
def update_user(id):
    #   Reciving Data
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    hash_password = generate_password_hash(password)
    act_usuario = {
        'username' : username,
        'email' : email,
        'password' : hash_password
    }
    
    mongo.db.usuarios.update_one({'_id' : ObjectId(id)}, {'$set' :  (act_usuario)})
    return f'Usuario: {id} Was Update Succesfull'


@app.errorhandler(404)
def page_not_found(error = None):
    response = jsonify({
        'message' : 'Resource Not Found' + request.url,
        'status' : 404
    })
    response.status_code = 404
    return response
    #return render_template('page_not_found.html'), 404

#   Inicializa el Servidor
if __name__ == "__main__":
    app.run(debug=True, port=3000)