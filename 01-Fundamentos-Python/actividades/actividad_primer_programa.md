# Actividad — Mi Primer Programa en Python

## Objetivo

Instalar Python correctamente, escribir y ejecutar tu primer programa, y entender cómo Python lee e imprime información en pantalla.

---

## Parte 1 — Verificar instalación (5 min)

Abre la terminal (CMD en Windows, Terminal en Mac/Linux) y ejecuta:

```
python --version
```

Debes ver algo como: `Python 3.12.0`

Si no funciona, prueba:
```
python3 --version
```

Si ninguno funciona → instalar Python desde **python.org** antes de continuar.

---

## Parte 2 — Primer programa (10 min)

Crea un archivo llamado `mi_primer_programa.py` y escribe este código **sin copiar y pegar** — escríbelo tú:

```python
# Mi primer programa en Python
nombre  = "Tu nombre aquí"
carrera = "Tu carrera aquí"
año     = 2025

print("=" * 35)
print(f"  Hola, soy {nombre}")
print(f"  Carrera: {carrera}")
print(f"  Año: {año}")
print("=" * 35)
print("¡Python instalado correctamente! 🐍")
```

**Cambia** `nombre` y `carrera` por tus datos reales.

**Ejecutar:**
```
python mi_primer_programa.py
```

---

## Parte 3 — Hacerlo interactivo (10 min)

Modifica el programa para que le **pregunte** al usuario su nombre en vez de tenerlo escrito fijo:

```python
# Versión interactiva
nombre  = input("¿Cuál es tu nombre? ")
carrera = input("¿Qué estudias? ")
año     = int(input("¿En qué año del curso estás? "))

print("=" * 40)
print(f"  Hola, soy {nombre}")
print(f"  Estudio: {carrera}")
print(f"  Año del curso: {año}")
print(f"  En 3 años terminaré en el {año + 3}")
print("=" * 40)
```

**Preguntas después de ejecutar:**
1. ¿Qué hace `input()`?
2. ¿Por qué usamos `int()` alrededor del segundo `input()`?
3. ¿Qué pasa si escribes letras cuando te pregunta el año?

---

## Reto extra

Sin instrucciones adicionales, modifica el programa para que también calcule e imprima:
- Cuántos años faltan para el 2030
- El doble de tu año actual

---

## Lo que aprendiste hoy

| Función | Para qué sirve |
|---|---|
| `print("texto")` | Mostrar texto en pantalla |
| `input("pregunta")` | Leer texto que escribe el usuario |
| `int(valor)` | Convertir texto a número entero |
| `f"Hola {variable}"` | Insertar variable dentro de texto |
| `# comentario` | Nota que Python ignora al ejecutar |
