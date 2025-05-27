"""
    Modulo collections
"""

from collections import Counter, defaultdict, namedtuple

# Counter cuenta los elementos de una tupla, palabra, o frases

numeros = [6,6,6,5,5,5,5,8,8,4,4,3,3,9]
print(Counter(numeros))

frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,2,2,2,3,3,3,3])
print(serie.most_common())                  #Ordena una lista con el total de apariciones de cada elemento


# Defaultdict

dic = defaultdict(lambda: "Vacio")
dic["Uno"] = "verde"
print(dic["Dos"])                           #Al no tener el valor "Dos", defaultdict creo el objeto y añade la descripcion deseada en este caso "Lambda"
print(dic)

# Namedtuple

Persona = namedtuple("Persona", ["nombre", "altura", "peso"])
persona1 = Persona("Brisa", 1.50, 48 )
print(persona1.altura)