from flask import Flask, render_template
#Con este comando estoy creando una nueva aplicacion
app = Flask(__name__)
#representa la paginan por defecto "una ruta"
@app.route("/")
#esta es la funcion que se va a mostrar en la pagina por defecto
#establecida en @app.route("/")
def index():
    headline = "Hello, World!"
    #Está retornando el index.html y ademas esta incorporando la variable headline
    #al index.html, envia la variable headline al html.
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Good bye!!"
    #Está retornando el index.html y ademas esta incorporando la variable headline
    #al index.html, envia la variable headline al html.
    return render_template("index.html", headline=headline)
