# Funcion index

texto = "Este es una prueba"
resultado = texto[0]
print(resultado)

resultado2 = texto.index("s") #Busca de izquierda a derecha
print(resultado2)

resultado3 = texto.rindex("a") #Busca de derecha a izquierda
print(resultado3)


# Extraer cadenas de texto

texto2 = "ABCDEFGHIJKLMNO"
fragmento = texto2[::-1] 
print(fragmento)