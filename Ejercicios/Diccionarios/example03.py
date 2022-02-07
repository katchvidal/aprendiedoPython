#   Ejercicio 03

"""
Programa: Comprube si una variable esta vacia y si esta vacia rellanarla con texto en minuscula e imprimirla en Mayuscula

"""


texto = ""

if len(texto.strip()) <= 0:
    #   Rellenar con texto en minuscula
    print("La variable no contiene texto introduce texto para rellenarla")
    relleno = input("Introduce el Texto: ")
    texto = relleno.lower()
    print(texto.upper())
else:
    print(f"La Variable Contiene Texto y es el siguiente: {texto.upper()} ")