#Esta funcion va a elevar al cuadrado un número
def square(x):
    return x * x

#Se define la funcion main para ejecutar el loop solo en este
#archivo y asi poder exportar la funcion square.
def main():
    for i in range(10):
        #Los {} indican el lugar que se va a mostrar los valores de
        #format(i, square(i)) respectivamente.
        print("{} squared is {}".format(i, square(i)))
#Si estoy corriendo este archivo en partucular entonces
#ejecuta la funcion main
if __name__ == "__main__":
    main()
    
