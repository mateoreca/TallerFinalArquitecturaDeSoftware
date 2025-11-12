from abc import ABC, abstractmethod
from prototype import Computadora, Telefono, Tableta

class ProductoFactory(ABC):
    @abstractmethod
    def crear_producto(self, nombre, precio, especificaciones):
        pass

class ComputadoraFactory(ProductoFactory):
    def crear_producto(self, nombre, precio, especificaciones):
        return Computadora(nombre, precio, especificaciones)

class TelefonoFactory(ProductoFactory):
    def crear_producto(self, nombre, precio, especificaciones):
        return Telefono(nombre, precio, especificaciones)

class TabletaFactory(ProductoFactory):
    def crear_producto(self, nombre, precio, especificaciones):
        return Tableta(nombre, precio, especificaciones)