# Interacción entre funciones

from random import shuffle

# Lista inicial

palitos = ["-","--","---","----"]

# Mezclar palitos

def mezclar_lista(lista):
    shuffle(lista)
    return lista

# Pedir intento

def pedir_intento():
    intento = "";
    while intento not in ["1","2","3","4"]:
        intento = input("Introduce tu intento del 1 al 4: ");
    return int(intento)

# Comprobar intento

def comprobar_intento(lista, intento):
    if lista[intento-1] == "-":
        print("Perdiste");
    else:
        print("Te salvaste");
    
    print(f"Te ha tocado {lista[intento-1]}")

# Juego

palitos_mezclados = mezclar_lista(palitos)
seleccion = pedir_intento()
print(mezclar_lista(palitos))
comprobar_intento(palitos_mezclados, seleccion)