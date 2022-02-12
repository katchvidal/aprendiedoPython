#   Manejar errores y excepciones


try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("El nombre no ha llegado correctamente try again")
finally:
    print("Tratamiento de Errores Correctamente ")


#   Crear la Lista
numeros = [13, 21 , 12, 2021, 2121, 7, 1, 2]
try:
    print("------   Busca un numero en la Lista --------------")
    search = int(input("Introduce el Numero para saber si esta en la lista: "))
    match = numeros.index(search)
    if match <= 0:
        print(f"El numero: {search} No esta dentro de la lista ")
    else:
        print("El numero esta dento de la lista ")
        print(numeros)
except:
    print(f"El numero: {search} no se encuentra en la Lista ")