#   Condicionales
"""
Condicional IF
si se cumple la condicion: ejecuta un grupo de instrucciones
si no se cumple la primera condicion se ejecutaran otro grupo de instrucciones
"""

# Ejemplo 01

print("############ Ejemplo 01  ################")
color = input("Introduce un color: ")
if color == "rojo":
    print("Tu color es Valido")
else :
    print("Tu color no es Valido")

# Operadores de Comparacion
"""
== igual
!= diferente
< menor que
> mayor que
<= menor igual que
>= mayor igual que
"""

#   Ejemplo 02
print("############ Ejemplo 01  ################")
year  = int(input("Introduce el año en el que estamos: "))

if year >= 2022:
    print("Estamos en el año 2022 en adelante")
else :
    print("El año es anterior a 2022")