# Actividad en Clase — Listas en Python

## Objetivo

Al terminar esta actividad, el estudiante será capaz de:

- Explicar qué es una lista y para qué sirve
- Crear listas con distintos tipos de datos
- Acceder a elementos usando índices
- Modificar el contenido de una lista

---

## ¿Qué es una lista?

Una lista es una colección ordenada de elementos. Piénsalo así: es como una fila de cajones numerados, donde cada cajón guarda un valor y tiene un número (índice) que empieza desde `0`.

```
índice →   0          1        2       3
lista  → ["manzana", "leche", "pan", "queso"]
```

- Se crea con corchetes `[ ]`
- Los elementos van separados por comas
- Se accede a cada elemento con su índice: `lista[0]`
- Puede guardar cualquier tipo de dato: texto, números, booleanos, etc.

---

## Código base

Copia este código en tu editor y úsalo como punto de partida:

```python
# ============================================
# ACTIVIDAD — Listas en Python
# ============================================

# --- PARTE 1: Crear listas ---
# Ya tienes estas listas creadas. Obsérvalas.

productos   = ["manzana", "leche", "pan", "queso"]
precios     = [1.5, 2.3, 0.8, 3.0]
disponible  = [True, True, False, True]

# Imprime cada lista y observa cómo se ven
print("Productos:", productos)
print("Precios:", precios)
print("Disponibles:", disponible)


# --- PARTE 2: Acceder por índice ---
# Completa las líneas siguientes para imprimir
# el primer producto, el tercer precio, y si el último producto está disponible

primer_producto = productos[0]         # "manzana"
# tercer_precio = precios[___]         # ← completa tú
# ultimo_disponible = disponible[___]  # ← completa tú (usa índice negativo)

print("Primer producto:", primer_producto)
# print("Tercer precio:", tercer_precio)
# print("Último disponible:", ultimo_disponible)


# --- PARTE 3: Modificar una lista ---
# El precio de "leche" subió a 2.8. Cámbialo.

# precios[___] = ___   # ← completa tú

print("Precios actualizados:", precios)


# --- PARTE 4: Agregar y eliminar ---
# Llegó un nuevo producto: "arroz" a 1.2, disponible.
# Agrégalo a cada lista.

# productos.append(___)
# precios.append(___)
# disponible.append(___)

print("Lista final de productos:", productos)
print("Total de productos:", len(productos))
```

---

## Tareas

### Parte 1 — Observar (sin modificar el código)
1. Ejecuta el código base tal como está.
2. Responde: ¿cuántos elementos tiene `productos`? ¿Qué tipo de dato tiene cada lista?

### Parte 2 — Acceder por índice
1. Completa las líneas comentadas para obtener el tercer precio y el último disponible.
2. **Antes de ejecutar**: escribe en papel qué crees que va a imprimir.
3. Ejecuta y compara con tu predicción.

### Parte 3 — Modificar
1. Cambia el precio de "leche" (índice 1) a `2.8`.
2. Imprime la lista completa para verificar el cambio.

### Parte 4 — Agregar
1. Usa `.append()` para agregar "arroz", su precio y su disponibilidad a cada lista.
2. Imprime `len(productos)` antes y después. ¿Qué hace `len()`?

---

## Pregunta de cierre (discusión grupal)

> Tienes 3 listas separadas para el mismo producto. ¿Qué problema puede causar esto si el inventario crece a 100 productos?

No hay respuesta incorrecta — el objetivo es pensar cómo organizar datos de forma lógica.

---

## Referencia rápida

| Operación | Código |
|---|---|
| Crear lista | `mi_lista = [1, 2, 3]` |
| Acceder por índice | `mi_lista[0]` |
| Último elemento | `mi_lista[-1]` |
| Modificar elemento | `mi_lista[0] = 99` |
| Agregar al final | `mi_lista.append(4)` |
| Tamaño de la lista | `len(mi_lista)` |
