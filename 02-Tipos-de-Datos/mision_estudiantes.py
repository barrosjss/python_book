# 🎓 Misión Crítica: Sistema de Registro de Estudiantes

print("--- SISTEMA DE REGISTRO UNIVERSITARIO ---")

# 1. Entrada de datos
nombre = input("Ingrese el nombre completo del estudiante: ")
edad = int(input("Ingrese la edad: "))
promedio = float(input("Ingrese el promedio acumulado: "))

# Lógica simple para la beca
tiene_beca_raw = input("¿Cuenta con beca? (si/no): ").lower()
tiene_beca = tiene_beca_raw == "si"

# 2. Procesamiento de datos (Ejemplo de lógica)
mayor_de_edad = edad >= 18

# 3. Salida de datos con f-strings (A estética premium)
print("\n" + "="*30)
print("       RESUMEN DEL REGISTRO")
print("="*30)
print(f"👤 Estudiante:  {nombre}")
print(f"🎂 Edad:        {edad} años ({'Mayor' if mayor_de_edad else 'Menor'} de edad)")
print(f"📊 Promedio:    {promedio:.2f}")
print(f"🎓 Becado:      {'✅ Si' if tiene_beca else '❌ No'}")
print("="*30)
print("Registro completado con éxito.\n")
