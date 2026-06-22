# Actividad — Tipos Primitivos en Acción

## Objetivo

Usar todos los tipos primitivos de Python en un programa real que procesa datos del usuario.

---

## Código base

Crea `tipos_en_accion.py` y completa los `___`:

```python
# Datos del usuario
nombre = input("Tu nombre: ")
edad   = int(input("Tu edad: "))
precio = float(input("Precio de un producto: "))

# Cálculos
precio_iva  = precio * 1.19
años_a_100  = 100 - edad
es_mayor    = edad >= 18

# Salida
print("=" * 40)
print(f"  Hola, {nombre.title()}")
print(f"  Edad: {edad} años")
print(f"  ¿Mayor de edad? {es_mayor}")
print(f"  Para llegar a 100: {años_a_100} años")
print(f"  Precio sin IVA:  ${precio:.2f}")
print(f"  Precio + 19% IVA: ${precio_iva:.2f}")
print("=" * 40)

# Verificar tipos
print(f"\nTipos:")
print(f"  nombre → {type(nombre)}")
print(f"  edad   → {type(edad)}")
print(f"  precio → {type(precio)}")
print(f"  es_mayor → {type(es_mayor)}")
```

---

## Preguntas después de ejecutar

1. ¿Qué pasa si escribes letras cuando te piden la edad?
2. ¿Por qué `is_mayor` es `bool` sin haberlo declarado así?
3. ¿Qué diferencia hay entre `precio` y `precio_iva` en tipo?

---

## Reto extra

Sin ayuda, agrega al programa:

- Cuántas letras tiene el nombre (sin espacios)
- El nombre en mayúsculas
- Si el precio con IVA supera $50, imprimir `"Producto caro"`, si no `"Precio accesible"`

---

## Referencia rápida

| Tipo | Ejemplo | Convertir |
|---|---|---|
| `str` | `"hola"` | `str(42)` |
| `int` | `25` | `int("25")` |
| `float` | `3.14` | `float("3.14")` |
| `bool` | `True` | `bool(0)` → `False` |
| `None` | `None` | — |
