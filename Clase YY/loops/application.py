from flask import Flask, render_template
#Con este comando estoy creando una nueva aplicacion
app = Flask(__name__)
#representa la paginan por defecto "una ruta"
@app.route("/")
def index():
    names = ["Alice", "Bob", "Charlie"]
    return render_template("index.html", names=names)
