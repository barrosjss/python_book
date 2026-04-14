# Bloque 3: Estructuras de Control en Python 🔄

> "En lógica usabas flechas para decidir el camino; en Python usamos la **identación** (sangría)."

En Python, el espacio al principio de la línea no es solo estético: **define qué bloques de código pertenecen a una estructura**. Olvida los `FIN-SI` o las llaves `{}`; aquí el orden lo da el espacio.

---

## 1. Condicionales: Toma de decisiones

### SI / SI-SINO (If-Else)
**En Pseudocódigo:**
```text
SI edad >= 18 ENTONCES
    ESCRIBIR "Eres mayor de edad"
SINO
    ESCRIBIR "Eres menor"
```

**En Python:**
```python
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor")
```

### SI-SINO SI (If-Elif-Else)
Para múltiples opciones usamos `elif` (abreviatura de *else if*).
```python
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

---

## 2. Bucles: El poder de la repetición

### Bucle MIENTRAS (While)
Se usa cuando no sabemos cuántas veces se repetirá algo, pero tenemos una condición.
```python
intentos = 0
while intentos < 3:
    print("Intentando conectar...")
    intentos += 1
```

### Bucle PARA (For)
En Python, el `for` es muy potente y se usa principalmente para recorrer secuencias o rangos.
```python
# Repetir 5 veces (del 0 al 4)
for i in range(5):
    print(f"Vuelta número {i}")
```

---

## ⚠️ La Regla de Oro: Dos Puntos y Sangría
Todas las estructuras en Python terminan en dos puntos (`:`) y la línea siguiente **debe** tener un espacio (4 espacios o un Tab).

---

## 🚀 Misión Crítica: Simulación de Cajero Automático

Vamos a implementar el núcleo del cajero que diseñaste en lógica.

**Requerimientos:**
1. Crear una variable `saldo` con un valor inicial.
2. Mostrar un menú al usuario: `1. Ver saldo`, `2. Retirar`, `3. Salir`.
3. Usar un bucle `while` para que el menú se repita hasta que el usuario elija `Salir`.
4. Usar `if-elif-else` para procesar la opción elegida.

---

## 📂 Recursos de este módulo
- `01_condicionales.py`: Ejemplos de comparaciones y lógica.
- `02_bucle_while.py`: Validaciones de entrada con bucles.
- `03_bucle_for.py`: Uso de `range()` y recorridos simples.
- `cajero_basico.py`: Implementación del reto.
