#   Modelo de Usuario
import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456",
)

print(database) 

class Usuario:

    def __init__(self, nombre, apellidos, email, PASSWORD):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.PASSWORD = PASSWORD

    def registrar(self):
        pass
    def loggin(self):
        pass
