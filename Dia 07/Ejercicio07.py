# Proyecto día 7
# Cuenta bancaria

class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):

    def __init__(self, nombre, apellido, cuenta, balance):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    # Metodo para print()
    def __str__(self):
        return f"Hola {self.nombre + " " +self.apellido} tu No. de cuenta es: {self.cuenta} con un saldo de: {self.balance}"
    
    # Metodo depositar
    def depositar(self):        
        saldoAgregar = int(input("Cantidad a depositar: "))
        self.balance = self.balance + saldoAgregar
        print(f"Tu nuevo saldo es: {self.balance}")

    # Metodo retirar
    def retirar(self):
        saldoRetirar = int(input("Cantidad que desea retirar: "))

        if saldoRetirar <= self.balance:
            self.balance = self.balance - saldoRetirar
            print(f"Retiro exitoso, su nuevo saldo es {self.balance}")
        else:
            print(f"No es posible retirar ya uqe ingreso una cantidad mayor a su saldo, su saldo es: {self.balance}")


cliente01 = Cliente("David", "Vilchis", 5563187248, 20000)

print(cliente01)
cliente01.depositar()
cliente01.retirar()
