"""
    Ejercicio 08
    Crear un programa para dar turnos, de diferentes areas
    para este caso sera una farmacia, con 3 areas perfumeria, farmcaia, y cosmeticos
    Tambien añadir decoradores
"""

# Decoradores para el ejercicio de turnos en una farmacia
def decorarTurno(funcion):

    def otraFuncion(turno):
        print("Turno asignado")
        funcion(turno)
        print("Aguarde y será atendido")
    
    return otraFuncion

#Codigo para asignar turnos

def asignarTurno(area):

    turnoA = 1
    turnoB = 1
    turnoC = 1
    
    while True:       

        #Perfumeria        
        if area == "a":            
            yield f"P - {turnoA}"
            turnoA += 1
        
        #Farmacia        
        elif area == "b":            
            yield f"F - {turnoB}"
            turnoB += 1

        #Cosmeticos
        elif area == "c":           
            yield f"C - {turnoC}"
            turnoC += 1

#Sistema de turnos

def sistemaTurnos():

    generadores = {"a": asignarTurno("a"), "b":asignarTurno("b"), "c":asignarTurno("c")}

    while True:
        print("\nSeleccione el área para tomar turno:")
        print("a) Perfumería")
        print("b) Farmacia")
        print("c) Cosméticos")
        print("d) Salir")

        opcion = input("Ingrese departamento: ").lower()

        if opcion == "d":
            print("Saliendo de sistema...")
            break
        elif opcion in generadores:
            turno = next(generadores[opcion])
            print(turno)
        else:
            print("Opcion no valida")
        