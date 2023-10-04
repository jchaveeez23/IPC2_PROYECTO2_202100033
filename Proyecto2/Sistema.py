import os

class Sistema:
    def __init__(self, nombre, altura, cantidad, drones):
        self.nombre = nombre
        self.altura = altura
        self.cantidad = cantidad
        self.drones = drones
        self.cabeza = None

    def __str__(self):
        return self.nombre

    def grafica(self):
        graph = "digraph G { \n"
        graph += "a0 [shape = none;label = <\n"
        graph += '<TABLE border="0" cellspacing="10" cellpadding="10" >\n'
        graph += "<TR>\n"
        graph += '<TD  bgcolor="#E2EFDA">Altura (mts)</TD>\n'
        actual = self.drones.primero
        graph += '<TD  bgcolor="#E2EFDA">' + actual.dato.nombre + "</TD>\n"
        while actual.siguiente:
            actual = actual.siguiente
            graph += '<TD  bgcolor="#E2EFDA">' + actual.dato.nombre + "</TD>\n"
        graph += "</TR>\n"

        for i in range(1, self.altura + 1):
            graph += "<TR>\n"
            graph += '<TD  bgcolor="#e9e9e9">' + str(i) + "</TD>\n"
            actual = self.drones.primero
            graph += '<TD  bgcolor="#e9e9e9">' + actual.dato.alturas.buscarInt(i).valor + "</TD>\n"
            while actual.siguiente:
                actual = actual.siguiente
                graph += '<TD  bgcolor="#e9e9e9">' + actual.dato.alturas.buscarInt(i).valor + "</TD>\n"
            graph += "</TR>\n"

        graph += "</TABLE>>;];\n"
        graph += "}"

        self.generarDot(str("sistema_" + self.nombre), graph)
    
    def generarDot(self, nombre, dot):
        with open(f"graphs/{nombre}.dot", "w") as f:
            f.write(dot)

        command = f"dot -Tpng graphs/{nombre}.dot -o graphs/{nombre}.png"
    
        os.system(command)