import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#En esta variable se almacena la ubicacion de mi base de datos y los parametros de esta
engine = create_engine("postgresql://postgres:DAmr160684@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
    #fetchall obtiene todos los elementos que contiene la consulta sql
    #la variable flights contiene todos los valores solicitados en el query SELECT...
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    #Recorriendo e imprimiendo la variable flights con flight
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")


if __name__ == "__main__":
    main()
