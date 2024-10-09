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
fragmento = texto2[::-1] #El primerparametro, es el inicio, segundo es hasta donde lo va a extraer, y el ultimo sera si necesitas que se extraiga de 2 en 2 o culquier otra combinación
print(fragmento)

