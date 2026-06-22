# Actividad — Sistema de Calificaciones

## Objetivo

Construir un programa que combina `while`, `if/elif/else` y `for` para registrar notas de estudiantes y generar un reporte.

---

## Código base

Crea `calificaciones.py` y completa los `___`:

```python
# Sistema de calificaciones
notas = []
continuar = "s"

# 1. Capturar estudiantes con while
while continuar.lower() == "s":
    nombre = input("Nombre del estudiante: ")
    nota   = float(input("Nota (0.0 - 5.0): "))

    # 2. Clasificar la nota con if/elif/else
    if nota >= 4.5:
        estado = "Excelente 🏆"
    elif nota >= ___:        # aprobado >= 3.0
        estado = "Aprobado ✅"
    else:
        estado = ___         # "Reprobado ❌"

    notas.append({"nombre": nombre, "nota": nota, "estado": estado})
    continuar = input("¿Agregar otro estudiante? (s/n): ")

# 3. Mostrar resultados con for
print("\n" + "=" * 45)
print(f"  {'ESTUDIANTE':<20} {'NOTA':>5}  ESTADO")
print("=" * 45)

for e in notas:
    print(f"  {e['nombre']:<20} {e['nota']:>5.1f}  {e['estado']}")

print("=" * 45)

# 4. Calcular promedio
promedio = sum(e["nota"] for e in notas) / len(notas)
print(f"\n  Promedio del grupo: {promedio:.2f}")
```

---

## Preguntas

1. ¿Qué pasa si el usuario escribe `"S"` (mayúscula) en lugar de `"s"`? ¿El `.lower()` lo resuelve?
2. ¿Qué error ocurre si no se registra ningún estudiante y se intenta calcular el promedio?
3. ¿Qué hace `:<20` y `:>5` en el f-string del reporte?

---

## Reto — Estadísticas completas

Sin código base, agrega al programa:

- Contar cuántos estudiantes aprobaron (nota >= 3.0)
- Contar cuántos reprobaron
- Encontrar el nombre del estudiante con la nota más alta

```python
aprobados  = 0
reprobados = 0
mejor      = notas[0]

for e in notas:
    if ___:
        aprobados += 1
    else:
        reprobados += 1
    if e["nota"] > mejor["nota"]:
        mejor = ___

print(f"\n  Aprobados : {aprobados}")
print(f"  Reprobados: {reprobados}")
print(f"  Mejor nota: {mejor['nombre']} con {mejor['nota']:.1f}")
```

---

## Referencia rápida

| Sentencia | Uso | Cuándo |
|---|---|---|
| `if / elif / else` | Tomar decisiones | Condición conocida |
| `while` | Repetir mientras | Condición indefinida |
| `for` | Recorrer iterable | Cantidad definida |
| `break` | Salir del bucle | Condición de parada interna |
| `continue` | Saltar iteración | Ignorar ciertos casos |
