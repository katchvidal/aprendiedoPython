#   Ejercicio Python 07

"""
Enunciado: mostrar todos los numeros impares entre dos numeros que elija el usuario

"""

num01 = int(input("Introduce el Primer Numero: "))
num02 = int(input("Introduce el Segundo Numero (Recuerda debe ser Mayor al numero 1): "))

if num01 > num02:
    print("Te recuerdo el segundo numero debe ser mayor al numero 1")
else:
    for contador in range(num01, num02 + 1):
        if contador%2 == 0:
            None
        else:
            print(contador)