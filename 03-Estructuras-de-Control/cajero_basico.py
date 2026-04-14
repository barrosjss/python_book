# 🏦 Misión Crítica: Simulación de Cajero Automático

saldo = 1000.0  # Saldo inicial
pin_correcto = "1234"
intentos = 3

print("--- BIENVENIDO AL BANCO PYTHON ---")

# Simple validación de PIN
while intentos > 0:
    pin = input("Ingrese su PIN de seguridad: ")
    if pin == pin_correcto:
        print("✅ Acceso concedido.")
        break
    else:
        intentos -= 1
        print(f"❌ PIN incorrecto. Le quedan {intentos} intentos.")

if intentos == 0:
    print("🚫 Tarjeta bloqueada. Contacte a su banco.")
else:
    # Menú Principal
    opcion = ""
    while opcion != "3":
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Ver Saldo")
        print("2. Retirar Dinero")
        print("3. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            print(f"💰 Su saldo actual es: ${saldo:.2f}")
        
        elif opcion == "2":
            retiro = float(input("¿Cuánto desea retirar?: "))
            if retiro > saldo:
                print("⚠️ Fondos insuficientes.")
            elif retiro <= 0:
                print("⚠️ Monto no válido.")
            else:
                saldo -= retiro
                print(f"✅ Retiro exitoso. Su nuevo saldo es: ${saldo:.2f}")
        
        elif opcion == "3":
            print("👋 Gracias por usar nuestros servicios. ¡Vuelva pronto!")
        
        else:
            print("⚠️ Opción no válida. Intente de nuevo.")
