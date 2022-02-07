nombre = "Katch Vidal"

#   Detectar Tipado
if not isinstance(nombre, float):
    print("La variable no es un numero con Decimales")

#   Limpiar Espacios
espacios = " 1 2  3 4 5 6 7 8 9 10   "
print(espacios)
print(espacios.strip())

#   Eliminar Variables
del espacios

#   Comprobar que las variables esten vacias
texto = "aaaaa  fffff       ccccc"
if len(texto) > 0 :
    print(f"La variable tiene {len(texto)} caracteres")
else : 
    print("La variable esta vacia")


#   Encontrar Caracteres
frase = "La Vida es Bella"
lugar  = frase.find("Vida")
print(f"La frase Buscada se encuentra en la posicion: {lugar} ")

#   Remplazar Frase o Palabra
new = frase.replace("Vida", "Motocicleta")
print(new)
print(new.upper())
print(new.capitalize())