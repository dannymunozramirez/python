import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker



app = Flask(__name__)
#En esta variable se almacena la ubicacion de mi base de datos y los parametros de esta
engine = create_engine("postgresql://postgres:DAmr160684@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

#Esta ruta muestra el book a flight.
@app.route("/")
def index():
    #selecciona todos los vuelos en la tabla flights
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)
#Recibe un post que esta asignado a esta funcion (book) en index.html en el form
@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""
    #almacena lo que se ingresa en el tag con nombre name de index.html
    name = request.form.get("name")
    try:
        #Este flight_id almacena el id del vuelo que selecciona el usuario en book a flight
        #lo transforma a integer.
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    if db.execute("SELECT * FROM flights WHERE id = id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No such flight with that id")
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    {"name": name, "flight_id": flight_id})

    db.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    """List all flights"""
    #Selecciona todo el contenido de la tabla flights y lo almacena en la variable flights
    #Luego lo pasa como una variable al flights.html
    flights = db.execute("SELECT * FROM flights").fetchall()
    #esta es la lista que muestra todos los vuelos de la tabla flights
    return render_template("flights.html", flights=flights)
#esta es la ruta contiene la funcion flight donde se muestra el contenido del vuelo que selecciono el
#ususuario y lo filtra por el id que se asigna al vuelo en la tabla flights.
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    #make sure flight exists.
    
    flight = db.execute("SELECT * FROM flights WHERE id = :id",
     {"id": flight_id}).fetchone()
    if flight is None:
        return render_template("error.html", message="No such flight.")

    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)





if __name__ == "__main__":
    main()
