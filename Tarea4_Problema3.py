"""
Tarea 4 Problema 3.
Bianca Gonzalez
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario
ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.

"""
import math
par = 0
inpar = 0
print("\n-Programa Que informa cuantos dígitos paras e impares tiene un número-")
while True:
    cadenae = input("\nIngrese un entero positivo: ")
    entero = int(cadenae)
    if entero > 0:
        for n in cadenae:
            digito = int(n)
            a = digito % 2
            if a == 0:
                par = par + 1
            else:
                inpar = inpar + 1

        print("Cantidad de cifras pares: ", par, "\nCantidad de Cifras impares: ", inpar)
        par = 0
        inpar =0


    elif entero == 0:
        print("-FIN DE PROGRAMA-")
        break

    else:
        print("\nError de datos, favor vuelva a ingresar el número \n ")