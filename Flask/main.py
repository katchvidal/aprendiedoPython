#   Importaciones de Paquetes Flask
from flask import Flask
from flask import render_template

#   Configuracion Inicial de Flas
app = Flask(__name__)


#   Rutas
@app.route('/')
def index():
    return "Aprendiendo Flask con Master en Python <h1> Home Page</h1>"

@app.route('/informacion')
def info():
    return "<h1> Pagina de Informacion con Flask</h1>"

@app.route('/contacto')
def contacto():
    return "<h1> Pagina de Contacto con Flask</h1>"



@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#   Inicializa el Servidor
if __name__ == "__main__":
    app.run(debug=True)