import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#En esta variable se almacena la ubicacion de mi base de datos y los parametros de esta
engine = create_engine("postgresql://postgres:DAmr160684@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():

    #selecciona los valores de las columnas id, origin, destination y duration de la base de datos y los muestra todos (fetchall)

    flights = db.execute("SELECT id, origin, destination, duration FROM flights").fetchall()
    #Recorriendo la lista y las columnas de la base de datos flight.id, flight.origin....
    for flight in flights:
        print(f"Flights {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes")
    #pide al usuario un flight id para saber que pasageros esta asociados a ese vuelo
    #convierte el valor en integer
    flight_id = int(input("\nFlight iD: "))
    #selecciona los valores de la base de datos flights y los compara con el valor ingresado por el usuario :id.
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id",
    {"id": flight_id}).fetchone()

    if flight is None:
        print("Error: No such flight!")
        return
    # como las bases de datos esta unidas con JOIN y sus id estan relacionados pasajeros y vuelos
    #se consulta con el valor ingresado por el usuario
    passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                            {"flight_id": flight_id}).fetchall()
    print("\nPassengers: ")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")

if __name__ == "__main__":
    main()
