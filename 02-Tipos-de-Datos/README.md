# Bloque 2: Tipos de Datos y Variables en Python 📊

> "En lógica definiste qué guardar; aquí aprenderás cómo guardarlo en la memoria de la computadora usando Python."

En Python, a diferencia de otros lenguajes, no necesitas declarar el tipo de dato explícitamente (es de **tipado dinámico**). Python es lo suficientemente inteligente para saber qué tipo de dato es según el valor que le asignes.

---

## 1. Variables: Tu contenedor de información
En pseudocódigo decíamos: `Definir nombre Como Texto`. En Python es tan simple como:
```python
nombre = "Juan"
```

## 2. Los Tipos Fundamentales

| Tipo | Pseudocódigo | Python | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Entero** | `Entero` | `int` | `edad = 25` |
| **Decimal** | `Real` / `Decimal` | `float` | `precio = 19.99` |
| **Texto** | `Texto` / `Cadena` | `str` | `ciudad = "Bogotá"` |
| **Booleano** | `Logico` | `bool` | `es_estudiante = True` |
| **Nulo** | `Nulo` | `None` | `resultado = None` |

---

## 3. Interactuando con el usuario: `input()`

Para que tus programas no sean estáticos, necesitamos recibir datos. 
> ⚠️ **IMPORTANTE**: Todo lo que entra por `input()` es tratado como **Texto (str)** por defecto.

```python
nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ") # Esto es un texto "25", no un número 25
```

---

## 4. Conversión de Tipos (Casting)
Si quieres hacer matemáticas con un `input()`, debes convertirlo:

```python
edad = int(input("¿Cuántos años tienes? ")) # Ahora sí es un número
estatura = float(input("¿Cuánto mides? "))
```

---

## 🚀 Misión Crítica: Sistema de Registro de Estudiantes

¿Recuerdas el ejercicio de lógica? Vamos a construirlo en Python.

**Requerimientos:**
1. Pedir el nombre del estudiante.
2. Pedir la edad (como entero).
3. Pedir el promedio de su última materia (como decimal).
4. Preguntar si tiene beca (usar una lógica de texto "si/no" por ahora).
5. Mostrar un resumen elegante usando **f-strings**.

**Ejemplo de f-string (la forma moderna de imprimir):**
```python
print(f"Estudiante: {nombre} | Edad: {edad}")
```

---

## 📂 Recursos de este módulo
- `01_variables.py`: Ejemplos de nombres válidos y asignación.
- `02_tipos_basicos.py`: Operaciones matemáticas y de texto.
- `03_entrada_datos.py`: Uso de `input` y conversiones.
- `mision_estudiantes.py`: Solución sugerida al reto.
