#!/usr/bin/env python3

# print("Hola Mundo")

numero = int(input("Ingrese un numero: "))
acumulador = 0
respuesta = 0

while acumulador <= numero:
    if acumulador == numero:
        print("El resultado es = ", respuesta)
        break
    else:
        acumulador = acumulador + 1
        respuesta = respuesta + acumulador
    print("Acumulador = ", acumulador)
    print("Respuesta = ", respuesta)

