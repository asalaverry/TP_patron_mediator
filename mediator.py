# Clase Mediator
class Mediator:
    def __init__(self):
        self.colega1 = None
        self.colega2 = None
        self.mensajes = []


    def set_colegas(self, colega1, colega2):
        self.colega1 = colega1
        self.colega2 = colega2

    def enviar(self, mensaje, colega):
        if colega == self.colega1:
            self.colega2.recibir(mensaje)
            self.mensajes.append(("Colega1", mensaje))
        elif colega == self.colega2:
            self.colega1.recibir(mensaje)
            self.mensajes.append(("Colega2", mensaje))

    def mostrar_chat(self):
        for remitente, mensaje in self.mensajes:
            print(f"{remitente}: {mensaje}")

# Clase Colega1
class Colega1:
    def __init__(self, mediator):
        self.mediator = mediator

    def enviar(self, mensaje):
        self.mediator.enviar(mensaje, self)

    def recibir(self, mensaje):
        print(f"Colega1 recibio un mensaje: {mensaje}")

# Clase colega2
class Colega2:
    def __init__(self, mediator):
        self.mediator = mediator

    def enviar(self, mensaje):
        self.mediator.enviar(mensaje, self)

    def recibir(self, mensaje):
        print(f"Colega2 recibio un mensaje: {mensaje}")




mediator = Mediator()

colega1 = Colega1(mediator)
colega2 = Colega2(mediator)

mediator.set_colegas(colega1, colega2)

def menu():
    while True:
        print("\nENVIO DE MENSAJES")
        print("1. Enviar mensaje a colega 2")
        print("2. Enviar mensaje a colega 1")
        print("3. Ver lista de mensajes")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            msg = input("Ingrese un mensaje: ")
            colega1.enviar(msg)
        elif opcion == "2":
            msg = input("Ingrese un mensaje: ")
            colega2.enviar(msg)
        elif opcion == "3":
            mediator.mostrar_chat()
        elif opcion == "4":
            break
        else:
            print("Ingrese una opcion valida")

menu()