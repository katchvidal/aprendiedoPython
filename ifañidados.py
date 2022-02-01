# IF AÑIDADOS

nombre = input("Introduce tu Nombre: ")
ciudad = input("Introduce tu ciudad: ")
edad = int(input("Introduce tu edad: "))
continente = input("Introduce tu continente: ")

if edad >= 18:
    # instrucciones
    if continente != "americano":
        print("Lamentablemente este pauta no esta disponible para tu contienente")
    else:
        print(f" {nombre} con Mayoria de edad de {ciudad} y del contienente {continente} puedes comunicarte al numero #123456 ")
else:
    #instrucciones
    print(f" {nombre} No tienes la edad suficiente para continuar con el resto del programa ")


print("########     Que dia de la semana es     ##############")

dia = int(input("introduce un numero del 1 al 7 para saber que dia de la semana es: "))

if dia == 1:
    print("Hoy es Lunes")
elif dia == 2:
    print("Hoy es Martes")
elif dia == 3:
    print("Hoy es Miercoles")
elif dia == 4:
    print("Hoy es Jueves")
elif dia == 5:
    print("Hoy es Viernes")
elif dia == 6:
    print("Hoy es Sabado")
else:
    print("Hoy es Domingo")
