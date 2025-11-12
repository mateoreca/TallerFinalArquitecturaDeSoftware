from abc import ABC, abstractmethod
from prototype import Computadora, Telefono, Tableta


class LineaProductosFactory(ABC):
    
    @abstractmethod
    def crear_computadora(self):
        pass
    
    @abstractmethod
    def crear_telefono(self):
        pass
    
    @abstractmethod
    def crear_tableta(self):
        pass


class LineaPremiumFactory(LineaProductosFactory):   
    def crear_computadora(self):
        return Computadora(
            "Premium Laptop Pro",
            3500,
            {
                "RAM": "32GB",
                "Procesador": "Intel i9 / M3 Max",
                "Almacenamiento": "2TB SSD",
                "GPU": "RTX 4080",
                "Pantalla": "4K OLED"
            }
        )
    
    def crear_telefono(self):
        return Telefono(
            "Premium Phone Ultra",
            1500,
            {
                "Pantalla": "6.7 pulgadas AMOLED",
                "Cámara": "200MP + Zoom 10x",
                "Procesador": "Snapdragon 8 Gen 3",
                "Batería": "5000mAh",
                "5G": True
            }
        )
    
    def crear_tableta(self):
        return Tableta(
            "Premium Tablet Pro",
            1800,
            {
                "Pantalla": "12.9 pulgadas Mini-LED",
                "Procesador": "M2 Pro",
                "Almacenamiento": "1TB",
                "Stylus": "Incluido",
                "5G": True
            }
        )


class LineaEstandarFactory(LineaProductosFactory):    
    def crear_computadora(self):
        return Computadora(
            "Estándar Laptop",
            1200,
            {
                "RAM": "16GB",
                "Procesador": "Intel i5 / Ryzen 5",
                "Almacenamiento": "512GB SSD",
                "GPU": "Integrada",
                "Pantalla": "Full HD"
            }
        )
    
    def crear_telefono(self):
        return Telefono(
            "Estándar Phone",
            600,
            {
                "Pantalla": "6.1 pulgadas AMOLED",
                "Cámara": "50MP + Zoom 3x",
                "Procesador": "Snapdragon 7 Gen 2",
                "Batería": "4000mAh",
                "5G": True
            }
        )
    
    def crear_tableta(self):
        return Tableta(
            "Estándar Tablet",
            500,
            {
                "Pantalla": "10.5 pulgadas LCD",
                "Procesador": "Snapdragon 870",
                "Almacenamiento": "256GB",
                "Stylus": "Compatible",
                "WiFi": True
            }
        )


class LineaEconomicaFactory(LineaProductosFactory):
    def crear_computadora(self):
        return Computadora(
            "Económica Laptop Basic",
            500,
            {
                "RAM": "8GB",
                "Procesador": "Intel i3 / Celeron",
                "Almacenamiento": "256GB SSD",
                "GPU": "Integrada",
                "Pantalla": "HD"
            }
        )
    
    def crear_telefono(self):
        return Telefono(
            "Económico Phone Lite",
            250,
            {
                "Pantalla": "6.0 pulgadas LCD",
                "Cámara": "13MP",
                "Procesador": "MediaTek Helio G85",
                "Batería": "3500mAh",
                "4G": True
            }
        )
    
    def crear_tableta(self):
        return Tableta(
            "Económica Tablet Basic",
            200,
            {
                "Pantalla": "8 pulgadas LCD",
                "Procesador": "MediaTek MT8768",
                "Almacenamiento": "64GB",
                "WiFi": True
            }
        )


def crear_familia_completa(factory):

    computadora = factory.crear_computadora()
    telefono = factory.crear_telefono()
    tableta = factory.crear_tableta()
    
    print(f"\n {computadora}")
    print(f" {telefono}")
    print(f" {tableta}")
    
    return computadora, telefono, tableta


"""
if __name__ == "__main__":
    print("\nAbstract Factory Pattern")
    
    # Crear línea Premium
    factory_premium = LineaPremiumFactory()
    productos_premium = crear_familia_completa(factory_premium)
    
    # Crear línea Estándar
    factory_estandar = LineaEstandarFactory()
    productos_estandar = crear_familia_completa(factory_estandar)
    
    # Crear línea Económica
    factory_economica = LineaEconomicaFactory()
    productos_economica = crear_familia_completa(factory_economica)
"""