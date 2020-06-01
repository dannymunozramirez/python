from flask import Flask
#Con este comando estoy creando una nueva aplicacion
app = Flask(__name__)
#representa la paginan por defecto "una ruta"
@app.route("/")
#esta es la funcion que se va a mostrar en la pagina por defecto
#establecida en @app.route("/")
def index():
    return "Hello, World!"

@app.route("/david")
def david():
    return("Hello, David")
#strign:name esta asignando lo que sea que el usuario ingrese en la pagina(URL)
#para dejarlo almacenado en la variable name. http://000.0.0.name
@app.route("/<string:name>")
def hello(name):
    #deja el nombre ingresado con la primera letra en mayúscula
    name = name.capitalize()
    return f"<h2>Hello, {name}!<h2>"
