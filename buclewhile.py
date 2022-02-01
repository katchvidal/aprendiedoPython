#   Bucle WHILE

"""
Siempre debe haber un contador, WHILE es una estructura de control que itera o repite la ejecucion de una serie de instruccioes tantas veces
como sea necesario hasta que deje de cumplirse la condicion
"""

iterador = 0
num01 = int(input("Introduce el numero de la Tabla de Multiplicar que deseas Ver de preferencia del 1 al 10: "))
if num01 > 0 and num01 > 10:
    print("Tu numero es Menor a 0 y Mayor a 10 por default asignaremos el numero 1 ")
    num01 = 1

while iterador <= 10:
    multiplicacion = num01 * iterador
    print(f" {num01} x {iterador} = {multiplicacion} ")
    iterador = iterador + 1