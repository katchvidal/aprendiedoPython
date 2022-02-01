"""
Tipos de datos para variables
"""

# Indica que la variable no contiene nada
nada = None

# Mostar tipo de dato
print(type(nada))
print("===========================================")

# Tipo de Dato Cadena String
cadena = "Hola Soy Katch Vidal"
print(cadena)
print(type(cadena))
print("===========================================")

# Tipo de Dato Entero
entero = 99
print(entero)
print(type(entero))
print("===========================================")

# Tipo de Dato Flotante
flotante = 99.22
print(flotante)
print(type(flotante))
print("===========================================")

# Tipo de Dato Boolean
boleano = True
print(boleano)
print(type(boleano))
print("===========================================")

# Tipo de Dato Array
Array = [100,1,True,99.31, "Katch"]
print(Array)
print(type(Array))
print("===========================================")

# Tipo de Dato Tupla Nunca cambia
Tupla = ("Master","en", "Python")
print(Tupla)
print(type(Tupla))
print("===========================================")

# Tipo de Dato Diccionario
Diccionario = {
    "Nombre" : "Katch",
    "Apellido" : "Vidal",
    "Curso": "Master en Python"
}
print(Diccionario)
print(type(Diccionario))
print("===========================================")

# Tipo de Dato Rango
rango = range(9)
print(rango)
print(type(rango))
print("===========================================")

# Concatenar Tipo de datos similares
# Convertir cada tipo de Dato
texto = "Texto Simple"
numerito = 776
print(str(numerito) + " texto") # Permite Concatenar un tipo de dato diferente de STR 
print(f" {str(numerito)} {texto}")
#   Escapar Comillas
mitexto = "en \"Python\""
#   Salto de Linea
mitexto2 = "Bievenido \n Alumnos"
print(mitexto)
print(mitexto2)