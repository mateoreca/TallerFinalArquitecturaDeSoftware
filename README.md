# Taller de Sistema de Gestión de Productos Electrónicos

Taller de implementación de **Patrones de Diseño Creacionales** para la gestión de productos electrónicos (Computadoras, Teléfonos y Tabletas) organizados en diferentes líneas comerciales.

---
##  Autores

Taller práctico de **Patrones de Diseño Creacionales**

**Mateo Rendon**

**Samuel Ibañez**

---

## Descripción

Sistema que permite crear y gestionar productos electrónicos utilizando cuatro patrones de diseño creacionales. El sistema controla:

- Configuración global de la aplicación (Singleton)
- Creación de productos individuales por tipo (Factory Method)
- Creación de familias completas de productos (Abstract Factory)
- Clonación de productos para generar variantes (Prototype)

---

## Patrones Implementados

### 1. Singleton - Configuración Global
**Archivo**: `singleton.py`

Garantiza una única instancia de configuración en toda la aplicación.

**Características**:
- Control de instancia única mediante `__new__`
- Configuración de: modo debug, idioma, entorno
- Comparte estado entre todas las referencias


### 2.  Factory Method - Fábricas Especializadas
**Archivo**: `factory.py`

Delega la creación de productos a fábricas especializadas por tipo.

**Características**:
- Clase abstracta `ProductoFactory` con método `crear_producto()`
- Tres fábricas concretas:
  - `ComputadoraFactory`
  - `TelefonoFactory`
  - `TabletaFactory`

---

### 3.  Abstract Factory - Familias de Productos
**Archivo**: `abstract_factory.py`

Crea familias completas de productos relacionados sin especificar clases concretas.

**Características**:
- Interfaz `LineaProductosFactory` con métodos abstractos
- Tres líneas de productos:

| Línea | Computadora | Teléfono | Tableta | Total |
|-------|------------|----------|---------|-------|
| **Premium** | $3,500 | $1,500 | $1,800 | **$6,800** |
| **Estándar** | $1,200 | $600 | $500 | **$2,300** |
| **Económica** | $500 | $250 | $200 | **$950** |



### 4. Prototype - Clonación de Productos
**Archivo**: `prototype.py`

Permite clonar productos existentes para crear variantes rápidamente.

**Características**:
- Clase base `ProductoElectronico` con método `clonar()`
- Usa `copy.deepcopy()` para clonación profunda
- Clases concretas: `Computadora`, `Telefono`, `Tableta`



---

##  Estructura del Proyecto

```
patrones-creacionales/
│
├── singleton.py           # Patrón Singleton
├── prototype.py           # Patrón Prototype + Clases base
├── factory.py            # Patrón Factory Method
├── abstract_factory.py   # Patrón Abstract Factory
├── main.py              # Demostración completa
└── README.md           # Esta documentación
```

---

