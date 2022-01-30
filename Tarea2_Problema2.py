"""Tarea 2 Problema 2
Bianca Gonzalez
Escriba un programa para crear una nueva cadena formada por los tres caracteres
del medio de una cadena de entrada."""


print("\n -Programa de Nueva Cadena Con los 3 Caracteres del Medio- \n")
cadena_i = input("Introduzca una cadena: ")
n = len(cadena_i)
cadena = cadena_i[int(n / 2 - 1)] + cadena_i[int(n / 2)] + cadena_i[int(n / 2 +1 )]
print("Nueva Cadena: ", cadena)