# Bloque 4: Funciones en Python 🧩

> "Divide y vencerás. Una función es una caja negra que recibe algo, lo procesa y te devuelve un resultado."

En Python, las funciones son la base de la organización. Nos permiten evitar repetir código y hacer que nuestros programas sean fáciles de leer y mantener.

---

## 1. Definiendo una Función
Usamos la palabra clave `def` seguida del nombre de la función y paréntesis.

**En Pseudocódigo:**
```text
FUNCION Saludar()
    ESCRIBIR "Hola Estudiante"
FIN FUNCION
```

**En Python:**
```python
def saludar():
    print("Hola Estudiante")

# Para que funcione, debo llamarla:
saludar()
```

---

## 2. Funciones con Parámetros (Entradas)
Las funciones pueden recibir información para trabajar con ella.

```python
def saludar_estudiante(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a la clase de Python.")

saludar_estudiante("Jesus")
```

---

## 3. El Retorno de Valores (`return`)
A veces no queremos que la función imprima algo, sino que nos **devuelva** un resultado para usarlo después.

```python
def sumar(a, b):
    resultado = a + b
    return resultado

total = sumar(10, 5)
print(f"El total de la suma es: {total}")
```

---

## 4. Buenas Prácticas: Docstrings
En Python, es ley documentar qué hace tu función usando tres comillas dobles `"""`.

```python
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dadas su base y altura.
    """
    return base * altura
```

---

## 🚀 Misión Crítica: Calculadora Modular

Vamos a crear una calculadora que no solo sume, sino que esté organizada por funciones.

**Requerimientos:**
1. Crear una función para cada operación básica: `sumar`, `restar`, `multiplicar`, `dividir`.
2. Crear una función `menu()` que muestre las opciones.
3. El programa principal debe pedir los números al usuario y llamar a la función correspondiente.

---

## 📂 Recursos de este módulo
- `01_basicas.py`: Funciones simples sin parámetros.
- `02_parametros.py`: Funciones que reciben datos.
- `03_retorno.py`: El uso de `return` y cómo capturarlo.
- `calculadora_pro.py`: Implementación del reto.
