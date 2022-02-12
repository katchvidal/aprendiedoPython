#   Aplicacion de Consola que Registre un Usuario y se pueda Loggear
#   1. Configuraciones Iniciales
#   Importaciones

from usuarios import acciones


doit = acciones.Acciones()


print("""
    Acciones Disponibles:
    -   Registro
    -   Login
""")



ACCIONES = input("¿Que deseas Hacer?: ").lower()
if ACCIONES == "registro":
    doit.registro()
elif ACCIONES == "login":
    doit.login()
