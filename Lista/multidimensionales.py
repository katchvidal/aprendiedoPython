#   Listas Multidimensionales

contactos = [
    [
        "Antonio",
        "antonio@correo.com"
    ],
    [
        "Luis",
        "Luis@correo.com"
    ],
    [
        "Pedro",
        "Pedro@correo.com"
    ],
    [
        "Antonio",
        "antonio@correo.com"
    ],
    [
        "Antonio",
        "antonio@correo.com"
    ],
    [
        "Antonio",
        "antonio@correo.com"
    ]
]

#   Imprimir


for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(f"Nombre: {elemento} ")
        else:
            print(f"Correo: {elemento} ")
    print("\n")