from Nodo import Nodo
from time import sleep
import xml.etree.ElementTree as ET
from Sistema import Sistema
from Dron import Dron
from Mensaje import Mensaje
from Instruccion import Instruccion


class ListaDoble:
    def __init__(self):
        self.primero = None
        self.cabezera = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato=dato)
        if self.primero is None:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def insertar_modo_pila(self, dato):
        if self.primero is None:
            self.primero = Nodo(dato=dato)
        else:
            actual = Nodo(dato=dato, siguiente=self.primero)
            self.primero.anterior = actual
            self.primero = actual

    def ordenar_alfabeticamente(self):
        if self.primero is None:
            return

        current = self.primero
        while current.siguiente:
            next_node = current.siguiente
            while next_node:
                if current.dato.lower() > next_node.dato.lower():
                    current.dato, next_node.dato = next_node.dato, current.dato
                next_node = next_node.siguiente
            current = current.siguiente

    def ordenar_alfabeticamente_nombre(self):
        if self.primero is None:
            return

        current = self.primero
        while current.siguiente:
            next_node = current.siguiente
            while next_node:
                if current.dato.nombre.lower() > next_node.dato.nombre.lower():
                    current.dato, next_node.dato = next_node.dato, current.dato
                next_node = next_node.siguiente
            current = current.siguiente

    def mostrar(self):
        actual = self.primero
        print(actual.dato.nombre, actual.dato.valor)
        while actual.siguiente:
            actual = actual.siguiente
            print(actual.dato.nombre, actual.dato.valor)

    def recorrer(self):
        if self.primero is None:
            print("La lista se encuentra vacía")
            return
        actual = self.primero
        print(
            "Nombre:",
            actual.dato.nombre,
            "cantidad de drones:",
            actual.dato.cantidad,
        )
        actual.dato.drones.recorrer_drones()
        while actual.siguiente:
            actual = actual.siguiente
            print(
                "Nombre:",
                actual.dato.nombre,
                "cantidad de drones:",
                actual.dato.cantidad,
            )
            actual.dato.drones.recorrer_drones()

    def recorrer_drones(self):
        if self.primero is None:
            print("La lista se encuentra vacía")
            return
        actual = self.primero
        print(
            "Nombre:",
            actual.dato.nombre,
        )
        actual.dato.alturas.recorrer_drones_alturas()

        while actual.siguiente:
            actual = actual.siguiente
            print(
                "Nombre:",
                actual.dato.nombre,
            )
            actual.dato.alturas.recorrer_drones_alturas()

    def recorrer_drones_alturas(self):
        if self.primero is None:
            print("La lista se encuentra vacía")
            return
        actual = self.primero
        print(
            "Nombre:",
            actual.dato,
        )
        while actual.siguiente:
            actual = actual.siguiente
            print(
                "Nombre:",
                actual.dato,
            )

    def recorrer_mensajes(self):
        if self.primero is None:
            return
        actual = self.primero
        print(
            "Nombre:",
            actual.dato.nombre,
            "Sistema de drones:",
            actual.dato.sistema_drones,
        )
        while actual.siguiente:
            actual = actual.siguiente
            print(
                "Nombre:",
                actual.dato.nombre,
                "Sistema de drones:",
                actual.dato.sistema_drones,
            )

    def buscarDato(self, nombre):
        if self.primero is None:
            print("La lista se encuentra vacía")
            return None
        nombre = nombre.lower()
        actual = self.primero
        if actual.dato == nombre:
            return actual.dato
        while actual.siguiente:
            actual = actual.siguiente
            if actual.dato == nombre:
                return actual.dato

    def buscar(self, nombre):
        if self.primero is None:
            print("La lista se encuentra vacía")
            return None
        nombre = nombre.lower()
        actual = self.primero
        if actual.dato.nombre == nombre:
            return actual.dato
        while actual.siguiente:
            actual = actual.siguiente
            if actual.dato.nombre == nombre:
                return actual.dato

    def buscarInt(self, nombre):
        if self.primero is None:
            print("La lista se encuentra vacía")
            return None
        actual = self.primero
        if actual.dato.nombre == nombre:
            return actual.dato
        while actual.siguiente:
            actual = actual.siguiente
            if actual.dato.nombre == nombre:
                return actual.dato

    def eliminar(self, nombre):
        nombre = nombre.lower()
        actual = self.primero
        if actual.dato.nombre == nombre:
            self.primero = actual.siguiente
            self.primero.anterior = None
            return
        while actual.siguiente:
            actual = actual.siguiente
            if actual.dato.nombre == nombre:
                actual.anterior.siguiente = actual.siguiente
                actual.siguiente.anterior = actual.anterior
                return

    def verTamano(self):
        actual = self.primero
        contador = 0
        while actual:
            contador = contador + 1
            actual = actual.siguiente

        return contador

    def leerArchivo(self, path):
        print("leyendo archivo", path)
        tree = ET.parse(path)
        root = tree.getroot()

        lista_drones = ListaDoble()
        for nodo in root.findall("listaDrones"):
            for nodoDron in nodo.findall("dron"):
                nombre = nodoDron.text
                lista_drones.insertar(nombre)

        for nodo in root.findall("listaSistemasDrones"):
            for nodoSistemaDrones in nodo.findall("sistemaDrones"):
                attributes = nodoSistemaDrones.attrib
                nombre = attributes["nombre"].lower()
                altura = int(nodoSistemaDrones.find("alturaMaxima").text)
                cantidadDrones = int(nodoSistemaDrones.find("cantidadDrones").text)
                drones = ListaDoble()
                for nodoContenido in nodoSistemaDrones.findall("contenido"):
                    nombre_dron = nodoContenido.find("dron").text
                    alturas = nodoContenido.find("alturas")
                    drone_alturas = ListaDoble()
                    for nodoAltura in alturas.findall("altura"):
                        altura2 = nodoAltura.attrib["valor"]
                        valor = nodoAltura.text
                        codigo = altura2 + "," + valor.upper()
                        intro = Instruccion(int(altura2), valor)

                        drone_alturas.insertar(intro)
                    drone = Dron(nombre_dron, drone_alturas)
                    drones.insertar(drone)

                sistema = Sistema(nombre, altura, cantidadDrones, drones)
                self.insertar(sistema)

        mensajes = ListaDoble()
        for nodo in root.findall("listaMensajes"):
            for nodoMensaje in nodo.findall("Mensaje"):
                attributes = nodoMensaje.attrib
                nombre = attributes["nombre"].lower()
                sistema_drones = nodoMensaje.find("sistemaDrones").text.lower()

                instrucciones = nodoMensaje.find("instrucciones")
                drones = ListaDoble()
                for nodoInstruccion in instrucciones.findall("instruccion"):
                    nodoInstruccionAtributos = nodoInstruccion.attrib
                    nombre_dron = nodoInstruccionAtributos["dron"].lower()
                    valor = nodoInstruccion.text
                    codigo = int(valor)
                    dron = Instruccion(nombre_dron, codigo)
                    drones.insertar(dron)

                mensaje = Mensaje(nombre, sistema_drones, ListaDoble(), drones, drones)
                mensajes.insertar(mensaje)

        return {
            "lista_drones": lista_drones,
            "lista_mensajes": mensajes,
        }

    def analizar(self, lista_sistemas):
        actual = self.primero
        sistema = lista_sistemas.buscar(actual.dato.sistema_drones)
        actual.dato.analizar(sistema)
        actual.dato.grafica()
        while actual.siguiente:
            actual = actual.siguiente
            sistema = lista_sistemas.buscar(actual.dato.sistema_drones)
            actual.dato.analizar(sistema)
            actual.dato.grafica()

    def generarXML(self):
        xml = ET.Element("respuesta")
        lista_mensajes = ET.SubElement(xml, "listaMensajes")
        actual = self.primero
        while actual:
            mensaje = ET.SubElement(lista_mensajes, "mensaje")
            mensaje.set("nombre", actual.dato.nombre)
            sistema_drones = ET.SubElement(mensaje, "sistemaDrones")
            sistema_drones.text = actual.dato.sistema_drones
            tiempo_optimo = ET.SubElement(mensaje, "tiempoOptimo")
            tiempo_optimo.text = str(actual.dato.tiempo_optimo)
            mensaje_recibido = ET.SubElement(mensaje, "mensajeRecibido")
            mensaje_recibido.text = actual.dato.mensaje
            instrucciones = ET.SubElement(mensaje, "instrucciones")
            tiempo = actual.dato.tiempo_optimo
            for i in range(1, tiempo + 1):
                tiempo_nodo = ET.SubElement(instrucciones, "tiempo")
                tiempo_nodo.set("valor", str(i))
                acciones = ET.SubElement(tiempo_nodo, "acciones")
                actual2 = actual.dato.salidas.primero
                while actual2:
                    instruccion = actual2.dato.alturas.buscarInt(i)
                    if instruccion:
                        dron = ET.SubElement(acciones, "dron")
                        dron.set("nombre", actual2.dato.nombre)
                        dron.text = instruccion.valor
                    actual2 = actual2.siguiente
            actual = actual.siguiente

        tree = ET.ElementTree(xml)
        tree.write("respuesta.xml")
        print("xml generado")
