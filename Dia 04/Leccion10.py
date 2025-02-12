# Metodo random y randint

from random import *

#Randint
aleatorio00 = randint(1,50);
print(aleatorio00)

#Aleatrio decimal con uniform
aleatorio01 = round(uniform(1,50),1);
print(aleatorio01)

#Random
aleatorio02 = random();
print(aleatorio02)

#Choice selleciona un dato de una lista
colores = ["azul", "rojo", "amarillo", "verde"]
aleatorio03 = choice(colores);
print(aleatorio03)

#Shuffle mezcla datos de una lista
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

# Comprension de listas

palabra = "python";
lista = [letra for letra in palabra];
lista2 = [n for n in range(0,21,2)];
print(lista);
print(lista2);
