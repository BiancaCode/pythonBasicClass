"""Tarea 2 Problema 4
Bianca Gonzalez
Escriba un programa que solicite al usuario ingresar dos cadenas y el programa de buscar si la
segunda cadena es parte de la primera cadena."""

print("\n -Programa de Busqueda de la Segunda Cadena en la Primera- \n")
s1 = input("Introduzca la primera cadena: ")
s2 = input("Introduzca la segunda cadena: ")
a = s1.find(s2)
if a == -1:
    print("No se encontró " + s2 + " en " + s1)
else:
    print("Si se encontró " + s2 + " en " + s1)
