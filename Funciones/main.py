#   Funciones en Python
"""
Funcion: conjunto de instrucciones agrupada bajo un nombre en concreto que puede reutilizarse tantas veces como sea necesario
Palabra Reservada: def
"""

#   Primer Hello World
def Hola():
    name = input("Introduce tu nombre: ")
    return print(f"Hola {name} desde tu primera funcion")

print("######   Ejemplo 01  ##########")
Hola() #    Puedes invocar una funcion tantas veces sean necesarias


#   Dos - Parametros
print("######   Ejemplo 02  ##########")

def showName( name ):
    print(f"Tu nombre es: {name} desde un parametro")

name = input("Introduce tu nombre: ")
showName(name)

print("######   Ejemplo 03  ##########")
def mayorEdad():
    edad = int(input("Introduce tu edad: "))
    if edad < 18:
        print(f"Eres Menor de Edad segun lo que digitaste {edad} ")
    else:
        print(f"Eres mayor de edad segun lo que digitaste: {edad} ")
mayorEdad()

print("######   Ejemplo 04  ##########")
def tablaMultiplicar():
    numero = int(input("Introduce el numero que deseas Multiplicar: "))
    for contador in range(0,11):
        operacion = numero * contador
        print(f" {numero} x {contador } = {operacion} ")
    print("\n")

tablaMultiplicar()