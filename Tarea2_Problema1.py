"""Tarea 2 Problema 1
Bianca Gonzalez
Escriba un programa para crear una nueva cadena compuesta por el primer carácter,
el del medio y último carácter de una cadena introducida por el usuario."""

print("\n -Programa de Nueva Cadena Con los carácteres 1ro, En medio y Último- \n")
cadena_i = input("Introduzca una cadena: ")
n = len(cadena_i)
cadena = cadena_i[0] + cadena_i[int(n/2)] + cadena_i[int(n-1)]
print("Nueva CAdena: ", cadena)