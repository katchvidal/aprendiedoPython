#   Multiples excepciones


try:
    numero = int(input("Introduce un numero para elevarlo al cuadrado: "))
    numerocuadrado = (numero * numero)
    print(f"El numero es: {numerocuadrado} ")
except Exception as e:
    print("Ha ocurrido un Error: ", type(e).__name__)