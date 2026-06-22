# Actividad — Agenda de Contactos

## Objetivo

Construir una agenda simple usando las 4 estructuras de datos: `dict`, `list`, `tuple` y `set`.

---

## Código base

Crea `agenda.py` y completa los `___`:

```python
# Un contacto completo usando las 4 estructuras
contacto = {
    "nombre":     "Tu nombre",
    "edad":       0,
    "telefono":   "000-0000",
    "correos":    ["principal@mail.com"],          # list
    "coordenadas": (4.7110, -74.0721),             # tuple
    "etiquetas":  {"amigo", "trabajo"}             # set
}

# 1. Agregar un segundo correo
contacto["correos"].append("otro@mail.com")

# 2. Agregar etiqueta al set
contacto["etiquetas"].add("familia")

# 3. Intentar agregar etiqueta duplicada — ¿qué pasa?
contacto["etiquetas"].add("amigo")
print(contacto["etiquetas"])   # ¿cambia?

# 4. Imprimir perfil formateado
print("=" * 40)
print(f"  {contacto['nombre'].upper():^36}")
print("=" * 40)
print(f"  Edad     : {contacto['edad']}")
print(f"  Teléfono : {contacto['telefono']}")
print(f"  Correos  : {contacto['correos']}")
print(f"  Etiquetas: {contacto['etiquetas']}")
print("=" * 40)

# 5. Buscar campo que no existe con .get()
print(contacto.get("direccion", "No registrada"))
```

---

## Reto — Lista de contactos

Sin código base, crea una lista de 3 contactos (cada uno es un dict) e imprime solo los nombres:

```python
agenda = [
    {"nombre": "Ana",   "telefono": "111-1111"},
    {"nombre": "Luis",  "telefono": "222-2222"},
    {"nombre": "María", "telefono": "333-3333"},
]

# Imprime solo los nombres
for ___ in agenda:
    print(___)
```

---

## Preguntas

1. ¿Por qué el set no agrega "amigo" si ya existe?
2. ¿Qué pasa si haces `contacto["coordenadas"][0] = 99`?
3. ¿Cuál es la diferencia entre `del contacto["edad"]` y `contacto.pop("edad")`?

---

## Referencia rápida

| Estructura | Crear | Agregar | Eliminar |
|---|---|---|---|
| `list` | `[1,2,3]` | `.append(x)` | `.remove(x)` |
| `tuple` | `(1,2,3)` | No se puede | No se puede |
| `dict` | `{"k":v}` | `d["k"]=v` | `del d["k"]` |
| `set` | `{1,2,3}` | `.add(x)` | `.discard(x)` |
