#   Ejercicio 02

"""
Escribir Porgrama que Añada Valores una lista mientras que su longitud sea Menor a 10 y luego Mostar la Lista

"""

lista = []

"""
for contador in range(0, 10):
    lista.append(contador)
    print(f"Agregando el Numero: {contador} ")

"""


contador = 0
while contador < 10:
    lista.append(contador)
    print(f"Agregando el Numero: {contador} ")
    contador = contador + 1

print(lista)