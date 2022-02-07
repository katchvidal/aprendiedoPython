#   Ejercicio de Diccionarios

"""
Hacer un programa de 8 numeros enteros.

- Recorrer la Lista y Mostrarla
- Hacerlo en una funcion
- Ordernarla y Mostrarla
- Mostar su Longitud
- Buscar Algun Elemento que el usuario pida por teclado

"""
def showList(lista, Obj = ""):
    resultado = None
    for resultado in lista:
        print(f"El {Obj} es: {resultado} ")

#   Crear la Lista
numeros = [13, 21 , 12, 2021, 2121, 7, 1, 2]

#   Recorrer y Mostrar la Lista
#print("-------  Recorrer y Mostrar Elemento de una Lista    --------")
#for numero in numeros:
#    print(f"El Numero es: {numero} ")

#showList(numeros, "Numero")
#longitud = len(numeros)
#print(f"La lista tiene una longitud de: {longitud} caracateres")
#print(numeros)
#numeros.sort()
#print(numeros)

print("------   Busca un numero en la Lista --------------")
search = int(input("Introduce el Numero para saber si esta en la lista: "))
match = numeros.index(search)
if match <= 0:
    print(f"El numero: {search} No esta dentro de la lista ")
else:
    print("El numero esta dento de la lista ")
    print(numeros)

