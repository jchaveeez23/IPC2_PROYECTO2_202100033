from Dron import Dron
from Instruccion import Instruccion
import os


class Mensaje:
    def __init__(
        self, nombre, sistema_drones, salidas, instruciones, copia_instruciones
    ):
        self.nombre = nombre
        self.sistema_drones = sistema_drones
        self.salidas = salidas
        self.instruciones = instruciones
        self.copia_instruciones = copia_instruciones
        self.tiempo_optimo = 2
        self.emitir_luz = False
        self.mensaje = ""

    def analizar(self, sistema):
        sistema.grafica()
        print("Analizando mensaje -----------------")
        print("mensaje", self.nombre)
        cantidad = sistema.cantidad
        cantidadx = 1
        actual = sistema.drones.primero
        self.verificarAlturas(actual.dato)
        while actual.siguiente:
            actual = actual.siguiente
            cantidadx = cantidadx + 1
            self.verificarAlturas(actual.dato)
            if cantidadx == cantidad:
                self.emitir_luz = False
                if self.instruciones.verTamano() == self.mensaje.__len__():
                    actual.siguiente = None
                else:
                    self.tiempo_optimo = self.tiempo_optimo + 1
                    cantidadx = 1
                    actual = sistema.drones.primero
                    self.verificarAlturas(actual.dato)

    def verificarAlturas(self, drone):
        # print("verificando altura en drone", drone.nombre)
        altura = self.verificarAltura(drone.alturas, drone)
        altura_instruccion = Instruccion(self.tiempo_optimo, altura.estado)
        salida = self.buscarSalida(drone.nombre)
        if salida == None:
            drone = Dron(drone.nombre, None)
            drone.alturas.insertar(Instruccion(1, "subir"))
            drone.alturas.insertar(altura_instruccion)
            self.salidas.insertar(drone)
        else:
            salida.alturas.insertar(altura_instruccion)

    def buscarSalida(self, nombre):
        if self.salidas.primero is None:
            return None

        actual = self.salidas.primero
        if actual.dato.nombre == nombre:
            return actual.dato
        while actual:
            if actual.dato.nombre == nombre:
                return actual.dato
            actual = actual.siguiente

        return None

    def verificarAltura(self, alturas, drone):
        if alturas.cabezera is None:
            alturas.cabezera = alturas.primero

        altura = alturas.cabezera.dato

        if drone.instruccion == None:
            instruccion = self.instruciones.buscar(drone.nombre)
            drone.instruccion = instruccion

        if drone.instruccion:
            if drone.instruccion.valor == altura.nombre:
                if self.emitir_luz:
                    altura.estado = "Esperar"
                else:
                    altura.estado = "Emitir Luz"
                    self.emitir_luz = True
                    self.mensaje = self.mensaje + altura.valor
                    drone.instruccion = None
                    self.instruciones.buscar(drone.nombre).nombre = "--" + drone.nombre

            elif drone.instruccion.valor > altura.nombre:
                altura.estado = "Subir"
                alturas.cabezera = alturas.cabezera.siguiente

            elif drone.instruccion.valor < altura.nombre:
                altura.estado = "Bajar"
                alturas.cabezera = alturas.cabezera.anterior
        else:
            altura.estado = "Esperar"
            drone.instruccion = None

        return altura

    def grafica(self):
        graph = "digraph G { \n"
        graph += "a0 [shape = none;label = <\n"
        graph += '<TABLE border="0" cellspacing="10" cellpadding="10" >\n'
        graph += "<TR>\n"
        graph += '<TD  bgcolor="#E2EFDA">Tiempo</TD>\n'
        actual = self.salidas.primero
        graph += '<TD  bgcolor="#E2EFDA">' + actual.dato.nombre + "</TD>\n"
        while actual.siguiente:
            actual = actual.siguiente
            graph += '<TD  bgcolor="#E2EFDA">' + actual.dato.nombre + "</TD>\n"
        graph += "</TR>\n"

        for i in range(1, self.tiempo_optimo + 1):
            graph += "<TR>\n"
            graph += '<TD  bgcolor="#e9e9e9">' + str(i) + "</TD>\n"
            actual = self.salidas.primero
            graph += (
                '<TD  bgcolor="#e9e9e9">'
                + actual.dato.alturas.buscarInt(i).valor
                + "</TD>\n"
            )
            while actual.siguiente:
                actual = actual.siguiente
                graph += (
                    '<TD  bgcolor="#e9e9e9">'
                    + actual.dato.alturas.buscarInt(i).valor
                    + "</TD>\n"
                )
            graph += "</TR>\n"

        graph += "</TABLE>>;];\n"
        graph += "}"

        self.generarDot(str("mensaje_" + self.nombre), graph)

    def generarDot(self, nombre, dot):
        with open(f"graphs/{nombre}.dot", "w") as f:
            f.write(dot)

        command = f"dot -Tpng graphs/{nombre}.dot -o graphs/{nombre}.png"

        os.system(command)

