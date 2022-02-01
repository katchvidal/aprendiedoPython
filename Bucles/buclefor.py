# Bucle FOR
"""
for variable in elemento(lista, rango, etc)
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0
for contador in range(0,10):
    print(f"Voy por el numero {contador}")

#   Calculadora Tablas de Multiplicar
print("#######  Tablas de MULTIPLICAR   ###########")
num01 = int(input("Introduce el numero de la Tabla de Multiplicar que quieres ver de preferencia del 1 al 10: "))
if num01 <= 1:
    print(" Tu numero es 0 y no se mostraria nada por default te mostraremos la tabla de 1 ")
    num01 = 1

print(f"Tabla de Multiplicar {num01} ")
for iterador in range(0,11):
    if num01 >= 11:
        print("Tu numero es de un rango muy alto introduce de nuevo un numero del 1 al 10 ")
        break
    multiplicacion = num01 * iterador
    print(f" {num01} x {iterador} = {multiplicacion} ")