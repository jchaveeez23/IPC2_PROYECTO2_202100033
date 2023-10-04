class Instruccion:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.estado = None

    def __str__(self):
        return self.nombre
