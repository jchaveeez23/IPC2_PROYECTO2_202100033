from Nodo import Nodo
from time import sleep
import xml.etree.ElementTree as ET

class ListaDoble2:
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

    def buscar(self, nombre):
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

    def verTamano(self):
        actual = self.primero
        contador = 0
        while actual:
            contador = contador + 1
            actual = actual.siguiente

        return contador
