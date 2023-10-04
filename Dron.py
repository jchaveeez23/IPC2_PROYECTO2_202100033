from ListaDoble2 import ListaDoble2
class Dron:
    def __init__(self, nombre, alturas):
        if alturas is None:
            self.alturas = ListaDoble2()
        else:
            self.alturas = alturas
        self.nombre = nombre
        self.altura = 0
        self.esperar = False
        self.estado = "Esperar"
        self.instruccion = None
        self.tiempo = 0

    def __str__(self):
        return self.nombre
        