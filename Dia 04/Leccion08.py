# Función if

letra = "b"

if letra == "a":
    print("Se cumplio el if y entro a codigo")

elif letra == "b":
    print("Entra a esta parte del codigo")

else:
    print("No entro a codigo")


# Ciclo For

lista = ["a", "b", "c"]

for letra in lista:
    print("Letra: " + letra)

palabra = "Python"

for letra in palabra:
    print(letra)


# Ciclo while

monedas = 5

while monedas > 0:

    print ( f"Tengo {monedas} monedas")
    monedas -= 1

else:
    print("Sin monedas")