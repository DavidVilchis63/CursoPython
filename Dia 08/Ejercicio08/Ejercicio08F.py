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
    pass