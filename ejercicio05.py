#   Ejercicion Python 05

"""
Mostrar todos los numeros que esten dentro de dos numeros seleccionados por el Usuario
"""
print("Mostrar Numero entre dos Parametros de preferencia del 0 al 100")
num01 = int(input("Introduce el Primer Numero: "))
num02 = int(input("Introduce el Segundo Numero: (recuerda no debe ser menor al numero 1): "))

contador = num01
if num01 > num02:
    print("El Numero 01 no debe ser Mayor al Numero 02 Try Again")
else:
    for contador in range(num01, num02 + 1):
        print(f"Numero: {contador} ")