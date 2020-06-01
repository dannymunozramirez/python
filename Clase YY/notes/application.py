from flask import Flask, render_template, request, session
from flask_session.__init__ import Session
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#global variable
notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    #Revisa si la lista esta vacia antes de agregar una nueva nota
    #Si la lista está vacía entonces inicializa una nueva lista para notas
    if session.get("notes") is None:
    #one specific session is going to take a empty list
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])
