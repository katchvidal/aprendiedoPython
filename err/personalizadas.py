#   Exepciones Personalizadas

nombre = input("Introduce el Nombre: ")
edad = int(input("Introduce la Edad: "))


if edad < 5 or edad > 110:
    raise ValueError("La edad introducida no es Real")
elif len(nombre) < 1:
    raise ValueError("El nombre no esta Completo")
else:
    print(f"Bienvenido al Master en Python {nombre} ")
