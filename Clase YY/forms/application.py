from flask import Flask, render_template, request
#Con este comando estoy creando una nueva aplicacion
app = Flask(__name__)
#representa la paginan por defecto "una ruta"
@app.route("/")
def index():
    return render_template("index.html")
#muestra el contenido en la ruta /hello y debe recibir un input de tipo POST
@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    resp = "Please fill the form"
    if request.method == "GET":
        return "Please submit the form instead"
    if not name:
            return resp
    else:
        #la variable name recibe el valor del contenido en el
        #formulario de nombre "name", ubicado en
        #el archivo index.html
        #request es un objeto importado de python.
        return render_template("hello.html", name=name)
