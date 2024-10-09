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

# Metodos para textos

nuevoTexto = "Lorem ipsum dolor sit amet consectetur adipiscing elit, duis justo auctor facilisis ultrices molestie, lobortis lectus quis tincidunt sollicitudin nisi."

resultado4 = nuevoTexto.upper()
resultado5 = nuevoTexto.lower()
resultado6 = nuevoTexto.split("a") #Creae lista cada espacio o si pones el caracter deseado, creara lista cada que aparesca ese caracter
print(resultado4)
print(resultado5)
print(resultado6)

a = "A"
b = "B"
c = "C"
d = "E"
e = " ".join([a,b,c,d]) #Junta las variables
print(e)

resultado7 = nuevoTexto.find("x") #Sirve para buscar caracteres, si no esta, el resultado sera un -1
resultado8 = nuevoTexto.replace("e","x")

print(resultado7)
print(resultado8)