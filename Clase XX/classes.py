#Definiendo una clase
class Point:
    #init funcion, cuando creo un nuevo punto, que informacion
    #necesito? "Parametros"
    #En este caso el parametro seria un objeto y dos variables
    #Esta es una funcion preestablecida de python.
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Point es el objeto asignado a la variable p y los parametros
#X e Y son los valores 3 y 5 respectivamente
# En conclusion la variable "p" invoca la clase "Point" y su funcion
# p = self(x, y)
p = Point(3, 5)
print(p.x)
print(p.y)
