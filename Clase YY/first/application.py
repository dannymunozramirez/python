from flask import Flask, render_template
#Con este comando estoy creando una nueva aplicacion
app = Flask(__name__)
#representa la paginan por defecto "una ruta"
@app.route("/")
#esta es la funcion que se va a mostrar en la pagina por defecto
#establecida en @app.route("/")
def index():
    return render_template("index.html")
