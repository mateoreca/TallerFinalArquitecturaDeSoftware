# Patrón Singleton

class ConfiguracionGlobal:
    __instancia = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instancia:
            cls.__instancia = super().__new__(cls, *args, **kwargs)
            cls.__instancia.modo = False
            cls.__instancia.idioma = "es"
            cls.__instancia.entorno = "producción"
        return cls.__instancia

    def __str__(self):
        return f"Configuración global -> modo_debug = {self.modo}, idioma = '{self.idioma}', entorno = '{self.entorno}"


'''
config1 = ConfiguracionGlobal()
config2 = ConfiguracionGlobal()

print(config1)
print(config2)
print(f"¿Misma instancia? {config1 is config2}")

config1.idioma = "en"
print(f"Config2.idioma después de modificar config1: {config2.idioma}")
'''

