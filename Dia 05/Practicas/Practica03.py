
#Ejercicio 3
#Escribe una función que requiera una cantidad indefinida deargumentos.
#0Lo que hará esta función es devolver True si enalgún momento se ha ingresado al numero cero repetido dos veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False

def dobleCero(*args):

    for i in range (len(args)-1):

        if i +1 == len(args):
            return False

        elif args[i] == 0 and args[i+1] == 0:
            return True
        
        else:
            i += 1
        
    return False
    
    


print(dobleCero(5,6,1,0,10))




