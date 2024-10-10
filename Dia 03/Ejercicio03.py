#Ejercicio del día 3, analizador de texto

texto1 = input("Ingrese un texto: ").lower()
letras = [input("Ingrese 1era letra: ").lower(),input("Ingrese 2da letra: ").lower(), input("Ingrese tres letras: ").lower()]


print("La letra 1 aparece:")
print(texto1.count(letras[0]))
print("La letra 2 aparece:")
print(texto1.count(letras[1]))
print("La letra 3 aparece:")
print(texto1.count(letras[2]))

texto2 = texto1.split()
print("Cuantas palabras tiene el texto: ")
print(len(texto2))

primeraletra = texto1[0:1]
segundaletra = texto1[-1:]

print("Primera letra:")
print(primeraletra)
print("Ultima letra:")
print(segundaletra)

texto2.reverse()
inverso = " ".join(texto2)
print(inverso)

print("python" in texto2)