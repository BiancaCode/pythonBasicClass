"""Tarea 7
Problema 1
Bianca
Se desea un programa que tenga una tupla que almacene 10 números enteros. 
Con la tupla el programa debe presenta el cuadrado de los números almacenados 
en la tupla."""

print("\nPrograma del cuadrado de un numero\n")

tupla = (0, 1, 2, 3, 5, 10, 11, 15, 20, 30, 50)

for numero in tupla:
    print(numero, "^2 = ", numero ** 2)
