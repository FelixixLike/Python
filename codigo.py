class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    pass

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        super().__init__(nombre,apellido)
        self.numero_cuenta =numero_cuenta
        self.balance = balance

    def depositar(self,cantidad):
        self.balance += cantidad
        

    def retirar(self,cantidad):
        self.balance -= cantidad


def crear_cliente():
    cliente = Cliente("juan", "peres", 12, 5000)



def inicio(cliente):
    pass

cliente = Cliente("f", "f", 5, 5)

cliente =Cliente("juan", "peres", 12, 5000)

print(cliente.balance)
