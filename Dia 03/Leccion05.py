# Propiedades de strings

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""

print("agua" in poema) #Esta en texto
print("agua" not in poema) # No esta entexto
print(len(poema)) #Numero de caracteres

# Listas

lista = ["a", "b", "c"]
lista2 = ["d", "e", "f"]
print(type(lista))

resultado = len(lista)
resultado1 = lista[0]

print(resultado)
print(resultado1)

print(lista + lista2)

lista2[0] ="alfa"
print(lista2)

lista.append("g")
print(lista)

eliminado = lista.pop()
print(lista)
print(eliminado)

lista3 = ["g","h","a","v","c"]
lista3.sort()
print(lista3)

lista4 = ["g","h","a","v","c"]
lista4.reverse()
print(lista4)
