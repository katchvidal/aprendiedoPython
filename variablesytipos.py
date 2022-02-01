"""
Una variable es un contenedor de informacion que guarda un dato, se puede crear infinidad de variables
que es un pedazo de memoria que se reserva con dicha informacion (No se puede empezar una variable con un numero pero si puede ser alfanumerico)
Python es un lenguaje debilmente tipado el cual puede ser perjudicial a la construccion de un codigo
"""

#   Variables
edad = 15
year = 2022
birthday = year - edad
print(birthday)
print("================================================")

# Concatenacion
nombre = "Katch"
apellidos = "Vidal"
web = "Katchvidal.mx"
print(nombre + " " + apellidos + " " + web)
# f permite interpolar cualquier variable dentro de un texto permite un codigo mas limpio
print(f"{nombre} {apellidos} {web} ")
# Metodo o funcion format
print("Hola me Llamo {} {} y mi web es: {}".format(nombre, apellidos, web))