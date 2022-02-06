#   Variables Globales y Locales

"""
Local: La variable local se define dentro de una funcion y no se puede usar fuera de la funcion a menos que se haga un return
Global: Variable definida fuera de una funcion y se puede usar tanto dentro como fuera
"""

#   Variable Global
frase = "Hello World"

def hello():
    print(frase)
    #   Variable Global convirtiendo a una Variable Local
    global frase02
    #   Variable Local
    frase02 = "Hello World 02"
    print(frase02)

print(frase)
hello()
print(frase02)