#   Ejercicio Python 04
"""
Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora

"""
print("Operaciones Basicas de una calculadora ( + - / * )")
num01 = int(input("Introduce el Primer Numero: "))
num02 = int(input("Introduce el Segundo Numero: "))

if num01 <= 0:
    print("Tu numero seleccionado fue 0 por default te asignaremos un numero entero = 1")
    num01 = 1
elif num02 <= 0:
    print("Tu numero seleccionado fue 0 por default te asignaremos un numero entero = 1")
    num02 = 1

print(f"Tus numeros seleccionados son Num01: {num01}, Num02: {num02} ")

#   Suma
print("#####    Suma    ######")
suma = num01 + num02
print(suma)
#   Resta
print("#####    Resta    ######")
resta = num01 - num02
if resta <= 0:
    print("El resultado es un numero negativo o Cero")
    print(resta)
else:
    print(resta)
#   Multiplicacion
print("#####    Multiplicacion    ######")
multiplicacion = num01 * num02
print(multiplicacion)
#   Division
print("#####    Division    ######")
Division = num01 / num02
print(Division)