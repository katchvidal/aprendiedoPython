"""

Un diccionario es un conjunto de valores pero en lugar de tener indice numerico tiene alfanumerico parecido a un objeto JSON

"""

#   Diccionario
personas = {
    "Nombre": "Katch"
}

#   Diccionario con Lista

contactos = [
    {
        "Nombre" : "Katch",
        "Apellido" : "Vidal1",
        "Email" : "katch1@correo.com"
    },
    {
        "Nombre" : "Katch",
        "Apellido" : "Vidal2",
        "Email" : "katch2@correo.com"
    },
    {
        "Nombre" : "Katch",
        "Apellido" : "Vidal3",
        "Email" : "katch3@correo.com"
    },
    {
        "Nombre" : "Katch",
        "Apellido" : "Vidal4",
        "Email" : "katch4@correo.com"
    },
    {
        "Nombre" : "Katch",
        "Apellido" : "Vidal5",
        "Email" : "katch5@correo.com"
    },
]

#print(personas)
#print(contactos)
#print(contactos[0]["Apellido"])

for contacto in contactos:
    print("El email es: {} ".format(contacto["Email"]))
    print("------------------")