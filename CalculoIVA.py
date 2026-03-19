#!/usr/bin/env python3

# Cálculo del IVA (Impuesto al Valor Agregado)
# Un sistema de facturación simple.

porcentaje_iva = 0.19
precio = int(input("Digita el precio del producto: "))

valor_iva = precio * porcentaje_iva
precio_final = precio + valor_iva

print("El valor del IVA es: ", valor_iva)
print("El precio final es: ", precio_final)