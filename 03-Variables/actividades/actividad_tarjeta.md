# Actividad — Tarjeta de Presentación

## Objetivo

Usar variables, `input()` y f-strings con formateo para generar una tarjeta de presentación profesional automática.

---

## Código base

Crea `tarjeta.py` y completa los `___`:

```python
# Capturar datos del usuario
nombre    = input("Nombre completo: ")
edad      = int(input("Edad: "))
profesion = input("Profesión: ")
salario   = float(input("Salario mensual ($): "))

# Cálculos
salario_anual  = salario * 12
salario_diario = salario / 30
años_jubilarse = 65 - edad

# Tarjeta formateada
print("\n" + "=" * 40)
print(f"  {nombre.upper():^36}")
print("=" * 40)
print(f"  Profesión  : {profesion}")
print(f"  Edad       : {edad} años")
print(f"  Jubilación : en {años_jubilarse} años")
print(f"  Salario/mes: ${salario:,.2f}")
print(f"  Salario/año: ${salario_anual:,.2f}")
print(f"  Salario/día: ${salario_diario:,.2f}")
print("=" * 40)
```

---

## Preguntas

1. ¿Por qué `edad` usa `int()` pero `salario` usa `float()`?
2. ¿Qué hace `:^36` en el f-string del nombre?
3. ¿Qué pasa si en años edad ya es mayor de 65?

---

## Reto extra

- Agrega el porcentaje que representa el salario diario del mensual: `{pct:.1%}`
- Si la persona ya tiene 65 años o más, mostrar `"¡Ya puede jubilarse!"` en lugar del conteo

---

## Referencia f-strings

| Especificador | Qué hace | Ejemplo |
|---|---|---|
| `:.2f` | 2 decimales | `3.14` |
| `:,` | Separador miles | `1,000` |
| `:,.2f` | Miles + 2 decimales | `1,234.50` |
| `:.1%` | Porcentaje 1 decimal | `19.8%` |
| `:^20` | Centrado en 20 chars | `     Ana     ` |
| `:<20` | Izquierda 20 chars | `Ana             ` |
| `:05d` | Rellenar ceros | `00042` |
