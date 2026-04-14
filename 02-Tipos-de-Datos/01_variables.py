# Ejemplos de Variables en Python

# 1. Asignación simple
nombre = "Jesus"
edad = 30
puntaje = 95.5
es_profe = True

# 2. Python es de tipado dinámico (puedes cambiar el tipo de una variable)
variable_loca = 10
print(f"Primero es: {type(variable_loca)}") # Mostrará <class 'int'>

variable_loca = "Hola"
print(f"Luego es: {type(variable_loca)}") # Mostrará <class 'str'>

# 3. Buenas prácticas (Snake Case)
nombre_completo = "Jesus Barros"
edad_del_estudiante = 20

# 4. Múltiple asignación
x, y, z = 1, 2, 3
print(f"x: {x}, y: {y}, z: {z}")
