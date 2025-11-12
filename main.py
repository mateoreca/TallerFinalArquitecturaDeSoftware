from singleton import ConfiguracionGlobal
from factory import ComputadoraFactory
from abstract_factory import LineaPremiumFactory

print("SISTEMA DE GESTIÓN DE PRODUCTOS\n")

# 1. Singleton
config = ConfiguracionGlobal()
print(f"Configuración: {config}\n")

# 2. Factory Method
factory = ComputadoraFactory()
pc = factory.crear_producto("Dell XPS", 1500, {"RAM": "16GB"})
print(f"Producto creado: {pc}\n")

# 3. Abstract Factory
linea = LineaPremiumFactory()
laptop = linea.crear_computadora()
print(f"Producto Premium: {laptop}\n")

# 4. Prototype
clon = laptop.clonar()
clon.precio = 4000
print(f"Producto clonado: {clon}")