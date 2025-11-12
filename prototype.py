import copy

class ProductoElectronico:
    def __init__(self, nombre, precio, especificaciones):
        self.nombre = nombre
        self.precio = precio
        self.especificaciones = especificaciones.copy() if isinstance(especificaciones, dict) else especificaciones
    
    def clonar(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        specs = ', '.join([f"{k}: {v}" for k, v in self.especificaciones.items()])
        return f"{self.__class__.__name__} '{self.nombre}' - ${self.precio} ({specs})"

class Computadora(ProductoElectronico):
    
    def __init__(self, nombre, precio, especificaciones):
        super().__init__(nombre, precio, especificaciones)
        self.tipo = "Computadora"


class Telefono(ProductoElectronico):
    def __init__(self, nombre, precio, especificaciones):
        super().__init__(nombre, precio, especificaciones)
        self.tipo = "Teléfono"


class Tableta(ProductoElectronico):
    def __init__(self, nombre, precio, especificaciones):
        super().__init__(nombre, precio, especificaciones)
        self.tipo = "Tableta"


"""
if __name__ == "__main__":
    laptop_original = Computadora(
        "MacBook Pro", 
        2500, 
        {"RAM": "16GB", "Procesador": "M2", "Almacenamiento": "512GB"}
    )
    
    
    laptop_variante = laptop_original.clonar()
    laptop_variante.nombre = "MacBook Pro 32GB"
    laptop_variante.especificaciones["RAM"] = "32GB"
    laptop_variante.precio = 3000
    
    print("Original:", laptop_original)
    print("Clonado:", laptop_variante)
    print(f"¿Son diferentes objetos? {laptop_original is not laptop_variante}")
"""    