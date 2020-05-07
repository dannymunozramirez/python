import datetime
from flask import Flask, render_template
#Con este comando estoy creando una nueva aplicacion
app = Flask(__name__)
#representa la paginan por defecto "una ruta"
@app.route("/")
def index():
    # El objeto now toma el valor del objeto datetime.now importado de python
    now = datetime.datetime.now()
    #Define com tipo condicional "if" que condiciones debe cumplir la variable
    #new_year, como que el mes debe ser 1 al igual que el dia
    #now.moth now es la variable de tipo objeto que usa los metodos del objeto
    #datetime.
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=new_year)
