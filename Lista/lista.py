#   Lista 01

"""
Definicion o Array : Colecciones de datos bajo un unico nombre podemos usar un indice numerico o alfanumerico 
"""

#   Definir Lista
from ast import While


Super_Heores = ["Batman", "Superman"]
Cantantes = list(("Bad Bunny", "Drake", "Los dos Hermanos", "Calibre 50", "Colmillo Norteño"))
years = list(range(1993, 2022))

#print(Super_Heores)
#print(Cantantes)
#print(years)

#   Indices de Elementos en una Lista
OneElement = Super_Heores[0]
#print(OneElement)
#print(Cantantes[1:3])
#print(Cantantes[1:])

#   Modificar un Indice
Cantantes[1] = "Gran Torino"
#print(Cantantes)

#   Pushear elementos en una Lista
Cantantes.append("Nickky Jam")
#print(Cantantes)

#   Recorrer Elementos de la Lista
nuevo_cantante = None

while nuevo_cantante != "stop":
    nuevo_cantante = input("Introduce tu cantante Favorito cuando quieras detener escribe 'stop': ")
    if nuevo_cantante != "stop":
        Cantantes.append(nuevo_cantante)
    else:
        print("Enterado ahora te mostraremos tu lista de Cantantes")

print("######## Lista de Cantantes  #########")
for cantante in Cantantes:
    print(f" {Cantantes.index(cantante) + 1 } : {cantante} ")

#   Eliminar Elementos de una Lista
