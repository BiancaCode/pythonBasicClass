"""Tarea 2 Problema 3
Bianca Gonzalez
Dadas dos cadenas, s1 y s2. Escriba un programa para crear una nueva cadena s3 agregando s2 en
medio de s1."""

print("\n -Programa de Nueva Cadena Con S2 en medio de S1- \n")
s1 = input("Introduzca una cadena S1: ")
s2 = input("Introduzca una cadena S2: ")
n1 = len(s1)
i = n1/2
mitad1 = s1[0: int(i)]
mitad2 = s1[int(i): int(n1)]
s3 = mitad1 + s2 + mitad2
print("La nueva cadena S3:", s3)