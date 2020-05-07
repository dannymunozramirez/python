import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#En esta variable se almacena la ubicacion de mi base de datos y los parametros de esta
engine = create_engine("postgresql://postgres:DAmr160684@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

def main():
    #Abriendo el archivo csv (comma, separate, value) y asignandolo a la variable f
    #el archivodebe estar en la misma carpeta y debe concordar con los tipo de datos de cada columna
    #tipo de ato, tipo de dato, tipo de dato
    f = open("flights.csv")
    #Leyendo cvs es un modulo de python para leer los archivos csv, leyendo el archivo csv
    reader = csv.reader(f)
    #Las tres variables se asignan a cada columna en el archivo csv almacenado en reader
    for origin, destination, duration in reader:
        #db.execute ejecuta la consulta de sql que ingresa los datos del archivo csv
        #:valor es el lugar que se asigna para ingresar los datos en la bd
        #Values :origin, :destination, :duration son iguales al key de diccionario.
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
            #Este diccionario esta diciendo a la consulta que es lo que tiene que llenar en cada uno de las posiciones asignadad
            #con las variables asignadas en el loop
            {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes")
    db.commit()# guarda los cambios que se realizaron

if __name__ == "__main__":
    main()
