# 🧮 Misión Crítica: Calculadora Modular

def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b

def restar(a, b):
    """Retorna la resta de dos números."""
    return a - b

def multiplicar(a, b):
    """Retorna el producto de dos números."""
    return a * b

def dividir(a, b):
    """Retorna el cociente. Maneja la división por cero."""
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def mostrar_menu():
    print("\n--- CALCULADORA MODULAR ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Programa Principal
while True:
    mostrar_menu()
    opcion = input("Elija una operación (1-5): ")
    
    if opcion == "5":
        print("Cerrando calculadora... ¡Adiós!")
        break
        
    if opcion in ["1", "2", "3", "4"]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == "1":
            print(f"➡️ Resultado: {sumar(num1, num2)}")
        elif opcion == "2":
            print(f"➡️ Resultado: {restar(num1, num2)}")
        elif opcion == "3":
            print(f"➡️ Resultado: {multiplicar(num1, num2)}")
        elif opcion == "4":
            print(f"➡️ Resultado: {dividir(num1, num2)}")
    else:
        print("⚠️ Opción no válida.")
