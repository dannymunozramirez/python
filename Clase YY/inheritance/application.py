from flask import Flask, render_template
#Con este comando estoy creando una nueva aplicacion
app = Flask(__name__)
#representa la paginan por defecto "una ruta"
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")
