"""
Tarea 6
Problema 4
Bianca
Se desea un programa que solicite al usuario 5 números enteros. El programa debe
presentar la tabla de multiplicar del O al 12 de los 5 números leídos.
"""
from pprint import pprint

print("Programa de Tablas de Multiplicar")

numeros = []
tabla = []

for i in range(5):
    numeros.append(int(input("Ingrese un numero: ")))

for n in numeros:
    for indice in range(13):
        tabla.append(str(n) + " X " + str(indice) + " = " + (str(n * indice)))

pprint(tabla)