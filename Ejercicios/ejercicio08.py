#   Ejercicio Python 08

"""
Enunciado: Porcentaje de un numero dado por el Usuario

"""


num01 = int(input("Introduce el Numero: "))
num02 = int(input("Introduce el Porcentaje del numero(Recuerda que los porcentajes son del 1 al 100): "))

if num02 > 100:
    print("Te recordamos los porcentajes son del 1 al 100")
elif num02 <= 0:
    print("Te recordamos los porcentajes son del 1 al 100")
else:
    porcentaje = num01 * (num02 / 100)
    print(f"El {num02}% del numero {num01} = {porcentaje} ")