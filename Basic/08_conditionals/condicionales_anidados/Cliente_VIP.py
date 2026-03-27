#!/usr/bin/env python3

tipo_cliente = ""
total_compras = 0
total_descuento = 0

total_compras = int(input("Digita el total de tus compras: "))
tipo_cliente = input("Digita el tipo de cliente: ")

if (tipo_cliente == "VIP")and(total_compras>500000):
    total_descuento = total_compras-(total_compras * 0.30)
    print("Tienes un descuento del 30%")
elif (tipo_cliente == "VIP")and(total_compras<500000):
    total_descuento = total_compras-(total_compras * 0.10)
    print("Tienes un descuento del 10%")
elif total_compras>500000:
    total_descuento = total_compras-(total_compras * 0.20)
    print("Tienes un descuento del 20%")
else:
    print("No tienes descuento")

print("El total de tus compras es: ", total_descuento)


