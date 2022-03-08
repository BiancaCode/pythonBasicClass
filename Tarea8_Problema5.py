"""Tarea 8
Problema 5
Bianca
Se le solicita crear un programa que tenga dos conjuntos formados por números
enteros.
El programa debe tener un menú con las siguientes opciones:
a. Realizar la operación de unión.
b. Realizar la operación de intersección.
c. Comparar si ambos conjuntos son iguales.
d. Indicar si el segundo conjunto es subconjunto del primero.
Con cada opción seleccionada el programa debe imprimir el resultado.
El usuario debe indicar cuando desea salir del programa."""
from pprint import pprint


def menu(c1, c2):
    while True:

        op = int(input("\nMenu\n1 Union \n2 Interseccion \n3 Comparar \n4 Subconjuto\n5 Salir: "))

        if op == 1:
            union = c1 | c2
            print("Resultado de la union:", union)

        if op == 2:
            interseccion = c1 & c2
            print("Resultado de la interseccion:", interseccion)

        if op == 3:
            print("Resultado de la comparacion: ", c1 == c2)

        if op == 4:
            print("Resultado de subconjunto: ", c2.issubset(c1))

        if op == 5:
            print("Fin del Programa")
            break

# ---------------------------------------------------------------------------------------------------------------------


print("\nPrograma de conjuntos de numeros enteros\n")

numeros1 = {10, 20, 30, 40, 50}

numeros2 = {10, 15, 20, 25, 30}

menu(numeros1, numeros2)