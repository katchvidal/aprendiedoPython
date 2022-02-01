#   Ejercicio Python 06

"""
Enunciado: Mostrar Tablas de Multiplicar del 1 al 10

"""

contador = 0
print("Tablas de Multiplicacion")
for cabecera in range(1,11):
    print(f"Tabla del {cabecera} ")
    for numero in range(1,11):
        multiplicacion = numero * cabecera
        print(f" {numero} x {cabecera} = {multiplicacion} ")
    
    print("\n")