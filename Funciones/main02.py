#   Parametro Opcionales

from cgitb import text


def getEmpleado(nombre = None, dni = None):
    print("Empleado")
    if dni != None and  nombre != None:
        print(f"Nombre: {nombre} ")
        print(f"DNI: {dni} ")


#getEmpleado("Katch", "123456")

#   Parametro Opciones y return o devolver datos de una funcion

#print("####################     Calculadora     ###############################")
#num01 = int(input("Introduce el Primer Valor: "))
#num02 = int(input("Introduce el Segundo Valor: "))
#operaciones = str(input("Que deseas Hacer [Suma, Resta, Multiplicacion, Division]: ")).lower()

def Calc(num01 = None, num02 = None, operaciones = None):

    if operaciones == "suma":
        operacion = num01 + num02
        return print(f" La Suma es = {operacion} ")
    if operaciones == "resta":
        operacion = num01 - num02
        return print(f" La Resta es = {operacion} ")
    if operaciones == "division":
        operacion = num01 / num02
        return print(f" La Division es = {operacion} ")
    if operaciones == "multiplicacion":
        operacion = num01 * num02
        return print(f" La Multiplicacion es = {operacion} ")


#Calc(num01, num02, operaciones)
#print(Calc(num01, num02, operaciones))


def getNombre(nombre = None):
    texto = f"El nombre es: {nombre} "
    return texto

def getApellido(apellido = None):
    texto = f"El Apellido es: {apellido} "
    return texto

def getNombreApellido(nombre, apellido):
    texto = getNombre(nombre) + " \n" + getApellido(apellido)
    return texto


print(getNombreApellido("Kia", "Vidal"))

