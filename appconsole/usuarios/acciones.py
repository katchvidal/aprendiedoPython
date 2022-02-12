#   Acciones de Usuarios
#   Crear Clase para cada Accion


class Acciones:
    def registro(self):
        print("Registrate en el Sistema ")
        NOMBRE = input("Cual es Tu Nombre: ").lower()
        APELLIDOS = input("Cual es Tu Apellido: ").lower()
        EMAIL = input("Cual es Tu Email: ").lower()
        PASSWORD = input("Cual es Tu Contraseña: ").lower()
    
    def login(self):
        print("Loggin en el Sistema ")
        EMAIL = input("Cual es Tu Email: ").lower()
        PASSWORD = input("Cual es Tu Contraseña: ").lower()