# Bloque 5: Listas y Colecciones en Python 📦

> "En lógica los llamamos arreglos; en Python, las **Listas** son las reinas de los datos. Son flexibles, potentes y fáciles de usar."

A diferencia de los arreglos tradicionales de otros lenguajes, las listas de Python pueden cambiar de tamaño dinámicamente y pueden contener diferentes tipos de datos al mismo tiempo.

---

## 1. Creando tu Listas
Usamos corchetes `[]`.

**En Pseudocódigo:**
```text
estudiantes = ["Ana", "Juan", "Pedro"]
```

**En Python:**
```python
frutas = ["Manzana", "Pera", "Mango"]
print(frutas)
```

### Acceso por índice
Recuerda que en programación empezamos a contar desde **0**.
```python
print(frutas[0]) # Manzana
print(frutas[2]) # Mango
```

---

## 2. Operaciones Comunes (Métodos)

| Operación | Método en Python | Ejemplo |
| :--- | :--- | :--- |
| **Agregar al final** | `.append()` | `frutas.append("Uva")` |
| **Eliminar por valor** | `.remove()` | `frutas.remove("Pera")` |
| **Eliminar por índice** | `.pop()` | `frutas.pop(0)` |
| **Saber cuántos hay** | `len()` | `cantidad = len(frutas)` |

---

## 3. Recorriendo la Lista
Esta es la forma más "Pythonica" de trabajar.

```python
for fruta in frutas:
    print(f"Me gusta comer {fruta}")
```

---

## 4. El Súper Poder de las Listas: Slicing
Python te permite extraer "rebanadas" de una lista fácilmente.

```python
numeros = [0, 1, 2, 3, 4, 5]
sub_lista = numeros[1:4] # Extrae [1, 2, 3]
```

---

## 🚀 Misión Crítica: Sistema de Inventario de Tienda

Vamos a crear un sistema para manejar los productos de una tienda.

**Requerimientos:**
1. Crear una lista vacía llamada `inventario`.
2. Crear funciones para:
    - `agregar_producto(nombre)`: Añade un producto a la lista.
    - `ver_inventario()`: Muestra todos los productos numerados.
    - `buscar_producto(nombre)`: Indica si el producto existe o no.
3. Crear un menú que permita al usuario gestionar su tienda.

---

## 📂 Recursos de este módulo
- `01_listas_basicas.py`: Creación y acceso.
- `02_metodos_listas.py`: Append, pop y remove.
- `03_recorridos.py`: Diferentes formas de usar el bucle for con listas.
- `gestion_inventario.py`: Implementación del reto.
