#   Ejercicio de Programacion Python 03
"""
Escribir un script que imprima por pantalla los primeros 60 numeros naturales al cuadrado

"""

contador = 0

#   While
print("#########    Bucle While   ################")
while contador <= 60:
    cuadrado = contador * contador
    print(f"El Cuadrado de {contador} = {cuadrado}  ")
    contador = contador + 1


print("#########    Bucle For   ################")
for contador in range (0,61):
    cuadrado = contador * contador
    print(f"El Cuadrado de {contador} = {cuadrado}  ")
