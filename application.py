<<<<<<< HEAD
from flask import Flask, render_template, request

app = Flask(__name__)

def estdiv(x, y, z):
        div = (x // y) * z//100
        return (div)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/service", methods=['GET', 'POST'])
def service():
    estimation = 0
    if request.method == "GET":
        return render_template('service.html', estimation=estimation)
    else:
        kwh = int(request.form.get('bill'))
        cov = int(request.form.get('cover'))
        panelMonth = (0.2*5*30)
        price = 0.15
        estimation = estdiv(kwh, panelMonth, cov)
        return render_template('service.html', estimation=estimation, panelMonth=panelMonth, price=price)

@app.route('/contact')
def contact():
    return render_template('contact.html')

=======
import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__)
#En esta variable se almacena la ubicacion de mi base de datos y los parametros de esta
engine = create_engine("postgresql://postgres:DAmr160684@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight"""

    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    if db.execute("SELECT * FROM flights WHERE id = id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id")
    db.execute("INSERT INTO passenger (name, flight_id) VALUES (:name, :flight_id)",
    {"name": name, "flight_id": flight_id})

    db.commit()
    return render_template("success.html")


if __name__ == "__main__":
    main()
>>>>>>> 04f67576948f798d09d7a24ad6b402c5211c3db5
