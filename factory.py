from prototype import Computadora, Telefono, Tableta

class ProductoFactory:
    def crear_computadora(self, nombre, precio, especificaciones):
        return Computadora(nombre, precio, especificaciones)
    
    def crear_telefono(self, nombre, precio, especificaciones):
        return Telefono(nombre, precio, especificaciones)
    
    def crear_tableta(self, nombre, precio, especificaciones):
        return Tableta(nombre, precio, especificaciones)